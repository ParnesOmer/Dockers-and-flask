import tempfile
import subprocess
from flask import Flask, request, jsonify
from logger import setup_logger

app = Flask(__name__)
logger = setup_logger("python_executor")


@app.route("/execute", methods=["POST"])
def execute_code():
    data = request.get_json()
    code = data['code']

    try:
        logger.info(f"Received code for execution")
        with tempfile.NamedTemporaryFile(suffix='.py', mode='w+', delete=False) as f:
            f.write(code)
            f.flush()

            result = subprocess.run(
                ['python3', f.name],
                capture_output=True,
                text=True,
                timeout=10
            )

        if result.stderr:
            logger.error(f"Error executing code: {result.stderr}")
            return jsonify({'error': result.stderr}), 500

        return jsonify({'Code output': f"{result.stdout}"}), 200

    except subprocess.TimeoutExpired:
        logger.error("Code execution timed out")
        return jsonify({'error': 'Code execution timed out'}), 500

    except Exception as e:
        logger.error(f"Error executing code: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    try:
        # Check if Python is available
        result = subprocess.run(['python3', '--version'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return jsonify({
                'status': 'healthy',
                'service': 'python-executor',
                'python_version': result.stdout.strip()
            }), 200
        else:
            return jsonify({
                'status': 'unhealthy',
                'service': 'python-executor',
                'error': 'Python not available'
            }), 500
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'service': 'python-executor',
            'error': str(e)
        }), 500


if __name__ == "__main__":
    # Start the Flask app
    logger.info("Starting Python Executor on port 5001")
    app.run(host="0.0.0.0", port=5001)

