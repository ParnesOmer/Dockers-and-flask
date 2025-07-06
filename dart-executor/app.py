import os
import tempfile
import subprocess
from flask import Flask, request, jsonify
from logger import setup_logger

app = Flask(__name__)
logger = setup_logger("dart_executor")


@app.route("/execute", methods=["POST"])
def execute_code():
    data = request.get_json()
    
    if not data or 'code' not in data:
        return jsonify({'error': 'No code provided'}), 400
    
    code = data['code']
    
    tmp_dir = tempfile.mkdtemp()
    dart_file_path = os.path.join(tmp_dir, "main.dart")
    
    try:
        logger.info("Received code for execution")
        
        # Write the Dart code to a temporary file
        with open(dart_file_path, "w") as f:
            f.write(code)
        logger.info("Code written to temporary file")
        
        # Execute the Dart code
        result = subprocess.run(
            ['dart', 'run', dart_file_path],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=tmp_dir
        )
        
        if result.returncode != 0:
            logger.error(f"Error executing code: {result.stderr}")
            return jsonify({'error': result.stderr}), 400
        
        logger.info("Code execution successful")
        return jsonify({'Code output': result.stdout}), 200
        
    except subprocess.TimeoutExpired:
        logger.error("Code execution timed out")
        return jsonify({'error': 'Code execution timed out'}), 500
        
    except Exception as e:
        logger.error(f"Error executing code: {str(e)}")
        return jsonify({'error': str(e)}), 500
        
    finally:
        try:
            # Clean up temporary files
            for filename in os.listdir(tmp_dir):
                os.remove(os.path.join(tmp_dir, filename))
            os.rmdir(tmp_dir)
        except Exception as cleanup_err:
            logger.warning(f"Cleanup failed: {cleanup_err}")


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    try:
        # Check if Dart is available
        result = subprocess.run(['dart', '--version'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return jsonify({
                'status': 'healthy',
                'service': 'dart-executor',
                'dart_version': result.stdout.strip()
            }), 200
        else:
            return jsonify({
                'status': 'unhealthy',
                'service': 'dart-executor',
                'error': 'Dart not available'
            }), 500
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'service': 'dart-executor',
            'error': str(e)
        }), 500


if __name__ == "__main__":
    # Start the Flask app
    logger.info("Starting Dart Executor on port 5003")
    app.run(host="0.0.0.0", port=5003) 