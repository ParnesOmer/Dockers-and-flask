# Multi-Language Code Execution System

A distributed system that executes code written in Python, Java, and Dart using Docker containers and Flask microservices.

## 🏗️ Architecture

The system consists of 5 Docker containers:

- **Router** (Port 5000) - Main orchestrator that handles file uploads and routes code execution
- **Python Executor** (Port 5001) - Executes Python code
- **Java Executor** (Port 5002) - Compiles and executes Java code  
- **Dart Executor** (Port 5003) - Executes Dart code
- **Client** (Port 5004) - Web interface for users

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd "Dockers and flask exercise"
   ```

2. **Build and start all services:**
   ```bash
   docker-compose up --build
   ```

3. **Access the web interface:**
   Open your browser and go to: `http://localhost:5004`

4. **Run tests (optional):**
   ```bash
   python test_system.py
   ```

## 📁 Project Structure

```
├── router/                 # Main orchestrator service
│   ├── app.py             # Flask application
│   ├── constants.py       # Configuration constants
│   ├── logger.py          # Logging setup
│   ├── Dockerfile         # Container configuration
│   └── requirements.txt   # Python dependencies
├── python-executor/       # Python code execution service
├── java-executor/         # Java code execution service
├── dart-executor/         # Dart code execution service
├── client/                # Web client application
│   ├── client.py          # Flask web application
│   ├── templates/         # HTML templates
│   │   ├── index.html     # Main upload page
│   │   ├── result.html    # Results display
│   │   └── health.html    # System health status
│   ├── Dockerfile         # Container configuration
│   └── requirements.txt   # Python dependencies
├── examples/              # Example code files for testing
│   ├── python_example.py  # Python demonstration
│   ├── java_example.java  # Java demonstration
│   ├── dart_example.dart  # Dart demonstration
│   └── README.md          # Examples documentation
├── logs/                  # Shared logging directory
├── test_system.py         # System test script
├── docker-compose.yml     # Multi-container orchestration
└── README.md              # This file
```

## 🎯 Usage

### Web Interface

1. **Upload Code Files:**
   - Go to `http://localhost:5004`
   - Click "Choose File" and select a `.py`, `.java`, or `.dart` file
   - Click "Upload File"

2. **Execute Code:**
   - Click "Execute All Code" to run all uploaded files
   - View results in a formatted display

3. **Monitor System Health:**
   - Click "System Health" to check all services status

### API Usage

#### Upload a file:
```bash
curl -X POST http://localhost:5000/upload \
  -F "code=@your_file.py"
```

#### Execute all uploaded code:
```bash
curl -X GET http://localhost:5000/execute
```

#### Direct code execution:
```bash
curl -X POST http://localhost:5004/api/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "print(\"Hello World!\")"}'
```

#### Check system health:
```bash
curl http://localhost:5004/health
```

## 🧪 Testing

### Automated Testing
Run the test script to verify all services are working:
```bash
python test_system.py
```

### Manual Testing with Examples
Use the provided example files in the `examples/` directory:

```bash
# Upload and test Python example
curl -X POST http://localhost:5000/upload \
  -F "code=@examples/python_example.py"

# Upload and test Java example
curl -X POST http://localhost:5000/upload \
  -F "code=@examples/java_example.java"

# Upload and test Dart example
curl -X POST http://localhost:5000/upload \
  -F "code=@examples/dart_example.dart"

# Execute all uploaded examples
curl -X GET http://localhost:5000/execute
```

## 🔧 Supported Languages

### Python (.py)
```python
print("Hello from Python!")
for i in range(5):
    print(f"Count: {i}")
```

### Java (.java)
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello from Java!");
        for (int i = 0; i < 5; i++) {
            System.out.println("Count: " + i);
        }
    }
}
```

### Dart (.dart)
```dart
void main() {
  print('Hello from Dart!');
  for (int i = 0; i < 5; i++) {
    print('Count: $i');
  }
}
```

## 🛡️ Security Features

- **Timeout Protection:** 10-second execution timeout
- **Temporary File Management:** Automatic cleanup after execution
- **Isolated Execution:** Each language runs in separate containers
- **Error Handling:** Comprehensive error catching and reporting

## 📊 Monitoring

### Health Endpoints
Each service provides a health check endpoint:
- Router: `http://localhost:5000/health`
- Python Executor: `http://localhost:5001/health`
- Java Executor: `http://localhost:5002/health`
- Dart Executor: `http://localhost:5003/health`

### Logs
All services log to the shared `./logs` directory:
- `router.log`
- `python_executor.log`
- `java_executor.log`
- `dart_executor.log`

## 🔍 Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Stop existing containers
   docker-compose down
   # Start fresh
   docker-compose up --build
   ```

2. **Permission denied:**
   ```bash
   # Fix log directory permissions
   sudo chmod 777 logs/
   ```

3. **Container build fails:**
   ```bash
   # Clean Docker cache
   docker system prune -a
   docker-compose up --build
   ```

4. **Test failures:**
   ```bash
   # Wait for services to start completely
   sleep 30
   python test_system.py
   ```

### Debug Mode
To run in debug mode, modify the Dockerfile CMD:
```dockerfile
CMD ["python", "-u", "app.py"]
```

## 📈 Performance

- **Execution Timeout:** 10 seconds per file
- **Concurrent Executions:** Supported
- **File Size Limit:** No explicit limit (Docker container limits apply)
- **Memory Usage:** Optimized with Alpine Linux base images

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is for educational purposes.

## 🙏 Acknowledgments

- Flask web framework
- Docker containerization
- Alpine Linux for lightweight containers 