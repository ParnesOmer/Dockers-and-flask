import os
import uuid
import requests
from flask import Flask, request, jsonify, send_file
from logger import setup_logger
from constants import Constants

app = Flask(__name__)
logger = setup_logger("router")


def get_or_create_uploads_dir():
    """Ensure the uploads directory exists."""
    uploads_dir = Constants.UPLOAD_FOLDER
    os.makedirs(uploads_dir, exist_ok=True)
    return uploads_dir


def get_language(filename):
    if filename.endswith('.py'):
        return 'python'
    elif filename.endswith('.java'):
        return 'java'
    elif filename.endswith('.dart'):
        return 'dart'
    else:
        raise ValueError("Unknown file type")


@app.route("/upload", methods=["POST"])
def upload_code():
    """Endpoint to upload a file."""
    if 'code' not in request.files:
        return jsonify({'error': 'No code file uploaded'}), 400
    logger.info(f"Received upload request")

    file = request.files['code']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    logger.info(f"Received file: {file.filename}")

    try:
        uploads_path = get_or_create_uploads_dir()
        file_id = str(uuid.uuid4())
        filename = f"{file_id}_{file.filename}"
        file_path = os.path.join(uploads_path, filename)
        file.save(file_path)
        logger.info(f"Found pending uploads")

        return jsonify({'file_id': file_id}), 200

    except Exception as e:
        logger.error(f"Error saving file: {str(e)}")
        return {"error": "Failed to save file"}, 500


@app.route("/execute", methods=["GET"])
def execute_code():
    """Endpoint to run the uploaded code."""
    uploads_path = get_or_create_uploads_dir()
    count_success = 0
    results = {}
    for filename in os.listdir(uploads_path):
        try:
            file_language = get_language(filename)
        except ValueError as e:
            logger.error(f"Error determining language for file {filename}: {str(e)}")
            continue

        executor_url = None
        if file_language == 'python':
            executor_url = Constants.EXECUTOR_URLS['python']
        elif file_language == 'java':
            executor_url = Constants.EXECUTOR_URLS['java']
        elif file_language == 'dart':
            executor_url = Constants.EXECUTOR_URLS['dart']

        code_path = os.path.join(uploads_path, filename)
        with open(code_path) as f:
            code_content = f.read()

        try:
            logger.info(f"Trying to execute code from {filename} using {file_language} executor")
            resp = requests.post(executor_url, json={'code': code_content})
            logger.info(f"Code execution response: {resp.status_code} - {resp.text}")
            if resp.status_code != 200:
                logger.error(f"Error executing code: {resp.text}")
                continue
            results[filename] = resp.json()
            count_success += 1
        except Exception as e:
            logger.error(f"Error executing code: {str(e)}")

    return jsonify({
            'message': 'Code execution completed',
            'success_count': count_success,
            'results': results
            }), 200


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    try:
        # Check if uploads directory is accessible
        uploads_path = get_or_create_uploads_dir()
        return jsonify({
            'status': 'healthy',
            'service': 'router',
            'uploads_directory': uploads_path
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'service': 'router',
            'error': str(e)
        }), 500


if __name__ == "__main__":
    # Start the Flask app
    logger.info("Starting Router on port 5000")
    app.run(host="0.0.0.0", port=5000)
