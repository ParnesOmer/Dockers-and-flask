/**
 * Dart Example for Multi-Language Code Execution System
 * This file demonstrates various Dart features that can be executed.
 */

/// Calculate the nth Fibonacci number
int fibonacci(int n) {
  if (n <= 1) {
    return n;
  }
  return fibonacci(n - 1) + fibonacci(n - 2);
}

/// Simple Person class to demonstrate OOP
class Person {
  final String name;
  final int age;
  final List<String> skills;

  Person(this.name, this.age, [List<String>? skills]) 
      : skills = skills ?? [];

  void addSkill(String skill) {
    skills.add(skill);
  }

  String get skillsAsString => skills.join(', ');

  @override
  String toString() {
    return 'Person{name: $name, age: $age, skills: $skills}';
  }
}

/// Main function - entry point of the program
void main() {
  print('🎯 Hello from Dart!');
  print('========================================');
  
  // Basic operations
  print('1. Basic Operations:');
  int a = 10, b = 5;
  print('   Addition: $a + $b = ${a + b}');
  print('   Subtraction: $a - $b = ${a - b}');
  print('   Multiplication: $a * $b = ${a * b}');
  print('   Division: $a / $b = ${a / b}');
  print('   Modulo: $a % $b = ${a % b}');
  
  // Lists and loops
  print('\n2. Lists and Loops:');
  List<int> numbers = [1, 2, 3, 4, 5];
  print('   Original list: $numbers');
  print('   Sum of list: ${numbers.reduce((a, b) => a + b)}');
  print('   Doubled numbers:');
  for (int num in numbers) {
    print('     $num * 2 = ${num * 2}');
  }
  
  // Function calls
  print('\n3. Function Calls:');
  print('   Fibonacci sequence (first 10 numbers):');
  for (int i = 0; i < 10; i++) {
    print('     F($i) = ${fibonacci(i)}');
  }
  
  // String operations
  print('\n4. String Operations:');
  String message = 'Hello, World!';
  print('   Original: \'$message\'');
  print('   Uppercase: \'${message.toUpperCase()}\'');
  print('   Lowercase: \'${message.toLowerCase()}\'');
  print('   Length: ${message.length} characters');
  print('   Contains "World": ${message.contains("World")}');
  
  // Object-oriented features
  print('\n5. Object-Oriented Features:');
  Person person = Person('Dart Developer', 28);
  person.addSkill('Dart');
  person.addSkill('Flutter');
  person.addSkill('Docker');
  print('   Person: $person');
  print('   Name: ${person.name}');
  print('   Skills: ${person.skillsAsString}');
  
  // Collections and functional programming
  print('\n6. Collections and Functional Programming:');
  List<String> fruits = ['apple', 'banana', 'orange', 'grape'];
  print('   Original fruits: $fruits');
  
  // Map operation
  List<String> upperFruits = fruits.map((fruit) => fruit.toUpperCase()).toList();
  print('   Uppercase fruits: $upperFruits');
  
  // Filter operation
  List<String> longFruits = fruits.where((fruit) => fruit.length > 5).toList();
  print('   Fruits with more than 5 letters: $longFruits');
  
  // Reduce operation
  String allFruits = fruits.reduce((a, b) => '$a, $b');
  print('   All fruits combined: $allFruits');
  
  // Null safety demonstration
  print('\n7. Null Safety:');
  String? nullableString = null;
  String nonNullableString = nullableString ?? 'Default Value';
  print('   Nullable string: $nullableString');
  print('   Non-nullable string: $nonNullableString');
  
  print('\n========================================');
  print('✅ Dart execution completed successfully!');
} 