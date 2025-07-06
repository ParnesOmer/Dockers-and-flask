import os


class Constants:
    BASE_DIR = os.getcwd()
    UPLOAD_FOLDER = '/tmp/uploads'

    EXECUTOR_URLS = {
        'python': 'http://python-executor:5001/execute',
        'java': 'http://java-executor:5002/execute',
        'dart': 'http://dart-executor:5003/execute'
    }
