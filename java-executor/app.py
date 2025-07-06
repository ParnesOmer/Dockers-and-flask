import os
import tempfile
import subprocess
from flask import Flask, request, jsonify
from logger import setup_logger

app = Flask(__name__)
logger = setup_logger("java_executor")


@app.route("/execute", methods=["POST"])
def execute_code():
    data = request.get_json()

    if not data or 'code' not in data:
        return jsonify({'error': 'No code provided'}), 400

    code = data['code']

    tmp_dir = tempfile.mkdtemp()

    class_name = "Main"
    java_file_path = os.path.join(tmp_dir, f"{class_name}.java")

    try:
        logger.info("Received code for execution")

        with open(java_file_path, "w") as f:
            f.write(code)
        logger.info("Code written to temporary file")

        compile_proc = subprocess.run(
            ["javac", f"{class_name}.java"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=tmp_dir
        )

        if compile_proc.returncode != 0:
            logger.error(f"Error compiling code: {compile_proc.stderr}")
            return jsonify({'error': compile_proc.stderr}), 400

        logger.info("Compilation successful, running the code")
        run_proc = subprocess.run(
            ["java", "-cp", tmp_dir, class_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if run_proc.returncode != 0:
            logger.error(f"Error running code: {run_proc.stderr}")
            return jsonify({'error': run_proc.stderr}), 400

        result = {
            "stdout": run_proc.stdout,
            "stderr": run_proc.stderr
        }

        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error writing code to temporary file: {str(e)}")
        return jsonify({'error': str(e)}), 500

    finally:
        try:
            for filename in os.listdir(tmp_dir):
                os.remove(os.path.join(tmp_dir, filename))
            os.rmdir(tmp_dir)
        except Exception as cleanup_err:
            logger.warning(f"Cleanup failed: {cleanup_err}")


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    try:
        # Check if Java is available
        result = subprocess.run(['java', '-version'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return jsonify({
                'status': 'healthy',
                'service': 'java-executor',
                'java_version': result.stderr.strip()  # Java version is in stderr
            }), 200
        else:
            return jsonify({
                'status': 'unhealthy',
                'service': 'java-executor',
                'error': 'Java not available'
            }), 500
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'service': 'java-executor',
            'error': str(e)
        }), 500


if __name__ == "__main__":
    # Start the Flask app
    logger.info("Starting Java Executor on port 5002")
    app.run(host="0.0.0.0", port=5002)
