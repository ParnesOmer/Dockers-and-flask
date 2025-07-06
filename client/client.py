from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configuration
ROUTER_URL = os.getenv('ROUTER_URL', 'http://localhost:5000')


@app.route('/')
def index():
    """
    Main page - displays the file upload form
    """
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload to the router
    """
    try:
        # Check if file was uploaded
        if 'code' not in request.files:
            flash('No file selected', 'error')
            return redirect(url_for('index'))

        file = request.files['code']
        
        # Check if file has a name
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('index'))

        # Send file to router
        files = {'code': (file.filename, file.stream, file.content_type)}
        response = requests.post(f"{ROUTER_URL}/upload", files=files, timeout=30)

        if response.status_code == 200:
            result = response.json()
            flash(f'File {file.filename} uploaded successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Upload failed: {response.text}', 'error')
            return redirect(url_for('index'))

    except requests.exceptions.RequestException as e:
        flash(f'Server communication error: {str(e)}', 'error')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'General error: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/execute', methods=['GET'])
def execute_code():
    """
    Execute all uploaded code files
    """
    try:
        # Send execution request to router
        response = requests.get(f"{ROUTER_URL}/execute", timeout=30)

        if response.status_code == 200:
            result = response.json()
            return render_template('result.html', result=result)
        else:
            flash(f'Execution failed: {response.text}', 'error')
            return redirect(url_for('index'))

    except requests.exceptions.RequestException as e:
        flash(f'Server communication error: {str(e)}', 'error')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'General error: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/health')
def health_check():
    """
    Check health status of all services
    """
    services = {
        'router': f"{ROUTER_URL}/health",
        'python-executor': f"{ROUTER_URL.replace(':5000', ':5001')}/health",
        'java-executor': f"{ROUTER_URL.replace(':5000', ':5002')}/health",
        'dart-executor': f"{ROUTER_URL.replace(':5000', ':5003')}/health"
    }

    status = {}
    
    for service_name, service_url in services.items():
        try:
            response = requests.get(service_url, timeout=5)
            if response.status_code == 200:
                status[service_name] = {"status": "healthy", "details": response.json()}
            else:
                status[service_name] = {"status": "unhealthy", "error": response.text}
        except Exception as e:
            status[service_name] = {"status": "unreachable", "error": str(e)}

    return render_template('health.html', services=status)


@app.route('/api/execute', methods=['POST'])
def api_execute():
    """
    API endpoint for direct code execution
    """
    try:
        data = request.get_json()
        
        if not data or 'code' not in data:
            return jsonify({"error": "Missing 'code' in JSON"}), 400

        # Send code to router for execution
        response = requests.post(f"{ROUTER_URL}/execute", json=data, timeout=30)
        
        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Server communication error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"General error: {str(e)}"}), 500


if __name__ == '__main__':
    print(f"Client starting on port 5004")
    print(f"Router URL: {ROUTER_URL}")
    app.run(host='0.0.0.0', port=5004, debug=True)
