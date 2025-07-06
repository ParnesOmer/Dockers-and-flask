#!/usr/bin/env python3
"""
Python Example for Multi-Language Code Execution System
This file demonstrates various Python features that can be executed.
"""

def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print("🐍 Hello from Python!")
    print("=" * 40)
    
    # Basic operations
    print("1. Basic Operations:")
    a, b = 10, 5
    print(f"   Addition: {a} + {b} = {a + b}")
    print(f"   Subtraction: {a} - {b} = {a - b}")
    print(f"   Multiplication: {a} * {b} = {a * b}")
    print(f"   Division: {a} / {b} = {a / b}")
    
    # Lists and loops
    print("\n2. Lists and Loops:")
    numbers = [1, 2, 3, 4, 5]
    print(f"   Original list: {numbers}")
    print(f"   Sum of list: {sum(numbers)}")
    print("   Doubled numbers:")
    for num in numbers:
        print(f"     {num} * 2 = {num * 2}")
    
    # Function calls
    print("\n3. Function Calls:")
    print("   Fibonacci sequence (first 10 numbers):")
    for i in range(10):
        print(f"     F({i}) = {fibonacci(i)}")
    
    # String operations
    print("\n4. String Operations:")
    message = "Hello, World!"
    print(f"   Original: '{message}'")
    print(f"   Uppercase: '{message.upper()}'")
    print(f"   Lowercase: '{message.lower()}'")
    print(f"   Length: {len(message)} characters")
    
    # Dictionary operations
    print("\n5. Dictionary Operations:")
    person = {
        "name": "Python Developer",
        "age": 25,
        "skills": ["Python", "Flask", "Docker"]
    }
    print(f"   Person: {person}")
    print(f"   Name: {person['name']}")
    print(f"   Skills: {', '.join(person['skills'])}")
    
    print("\n" + "=" * 40)
    print("✅ Python execution completed successfully!")

if __name__ == "__main__":
    main() 