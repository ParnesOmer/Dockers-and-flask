# Dart Executor

This is the Dart code execution service for the multi-language code execution system.

## Features

- Executes Dart code in a sandboxed environment
- Supports timeout protection (10 seconds)
- Automatic temporary file cleanup
- Comprehensive error handling and logging
- Health check endpoint for monitoring

## API Endpoints

### POST /execute
Executes Dart code provided in the request body.

**Request Body:**
```json
{
  "code": "void main() { print('Hello World!'); }"
}
```

**Response:**
```json
{
  "Code output": "Hello World!\n"
}
```

### GET /health
Returns the health status of the service and Dart version information.

**Response:**
```json
{
  "status": "healthy",
  "service": "dart-executor",
  "dart_version": "Dart VM version: 3.x.x"
}
```

## Docker Configuration

The service runs on port 5003 and includes:
- Python 3.9 base image
- Dart SDK installation
- Flask web framework
- Logging configuration

## Usage

1. Start the service with Docker Compose:
   ```bash
   docker-compose up dart-executor
   ```

2. Send Dart code for execution:
   ```bash
   curl -X POST http://localhost:5003/execute \
     -H "Content-Type: application/json" \
     -d '{"code": "void main() { print(\"Hello from Dart!\"); }"}'
   ```

## Error Handling

The service handles various error scenarios:
- Invalid JSON input
- Code execution timeouts
- Dart compilation errors
- System resource issues

All errors are logged and returned with appropriate HTTP status codes. 