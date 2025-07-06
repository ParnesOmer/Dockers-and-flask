# Code Examples

This directory contains example code files for testing the Multi-Language Code Execution System.

## 📁 Available Examples

### 🐍 Python Example (`python_example.py`)
Demonstrates Python features including:
- Basic arithmetic operations
- Lists and loops
- Function calls (Fibonacci sequence)
- String operations
- Dictionary operations

### ☕ Java Example (`java_example.java`)
Demonstrates Java features including:
- Basic arithmetic operations
- Arrays and loops
- Function calls (Fibonacci sequence)
- String operations
- Object-oriented programming (Person class)

### 🎯 Dart Example (`dart_example.dart`)
Demonstrates Dart features including:
- Basic arithmetic operations
- Lists and loops
- Function calls (Fibonacci sequence)
- String operations
- Object-oriented programming
- Collections and functional programming
- Null safety

## 🚀 How to Use

### Method 1: Web Interface
1. Start the system: `docker-compose up --build`
2. Open: `http://localhost:5004`
3. Upload any example file
4. Click "Execute All Code"

### Method 2: API
```bash
# Upload Python example
curl -X POST http://localhost:5000/upload \
  -F "code=@examples/python_example.py"

# Upload Java example
curl -X POST http://localhost:5000/upload \
  -F "code=@examples/java_example.java"

# Upload Dart example
curl -X POST http://localhost:5000/upload \
  -F "code=@examples/dart_example.dart"

# Execute all uploaded code
curl -X GET http://localhost:5000/execute
```

### Method 3: Direct Execution
```bash
# Execute Python code directly
curl -X POST http://localhost:5004/api/execute \
  -H "Content-Type: application/json" \
  -d @examples/python_example.py

# Execute Java code directly
curl -X POST http://localhost:5004/api/execute \
  -H "Content-Type: application/json" \
  -d @examples/java_example.java

# Execute Dart code directly
curl -X POST http://localhost:5004/api/execute \
  -H "Content-Type: application/json" \
  -d @examples/dart_example.dart
```

## 🧪 Testing Different Scenarios

### Success Cases
- All example files should execute successfully
- Each demonstrates different language features
- Output should be well-formatted and readable

### Error Cases (for testing)
You can create files with errors to test error handling:

**Python Error Example:**
```python
print("This will work")
print(undefined_variable)  # This will cause an error
```

**Java Error Example:**
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("This will work");
        System.out.println(undefinedVariable);  // This will cause an error
    }
}
```

**Dart Error Example:**
```dart
void main() {
  print('This will work');
  print(undefinedVariable);  // This will cause an error
}
```

## 📊 Expected Output

Each example should produce output similar to:

```
🐍 Hello from Python!
========================================
1. Basic Operations:
   Addition: 10 + 5 = 15
   Subtraction: 10 - 5 = 5
   Multiplication: 10 * 5 = 50
   Division: 10 / 5 = 2.0
...
✅ Python execution completed successfully!
```

## 🔧 Custom Examples

Feel free to create your own examples! Just ensure:
- Python files end with `.py`
- Java files end with `.java` and contain a `Main` class
- Dart files end with `.dart` and contain a `main()` function
- Code is safe to execute (no infinite loops, reasonable resource usage)

## ⚠️ Important Notes

- **Timeout:** Code execution is limited to 10 seconds
- **Security:** Code runs in isolated containers
- **File Size:** Keep files reasonably sized
- **Dependencies:** Only standard library features are available 