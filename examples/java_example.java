/**
 * Java Example for Multi-Language Code Execution System
 * This file demonstrates various Java features that can be executed.
 */
public class Main {
    
    /**
     * Calculate the nth Fibonacci number
     */
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n-1) + fibonacci(n-2);
    }
    
    /**
     * Main method - entry point of the program
     */
    public static void main(String[] args) {
        System.out.println("☕ Hello from Java!");
        System.out.println("========================================");
        
        // Basic operations
        System.out.println("1. Basic Operations:");
        int a = 10, b = 5;
        System.out.println("   Addition: " + a + " + " + b + " = " + (a + b));
        System.out.println("   Subtraction: " + a + " - " + b + " = " + (a - b));
        System.out.println("   Multiplication: " + a + " * " + b + " = " + (a * b));
        System.out.println("   Division: " + a + " / " + b + " = " + (a / b));
        
        // Arrays and loops
        System.out.println("\n2. Arrays and Loops:");
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.print("   Original array: [");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i]);
            if (i < numbers.length - 1) System.out.print(", ");
        }
        System.out.println("]");
        
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        System.out.println("   Sum of array: " + sum);
        
        System.out.println("   Doubled numbers:");
        for (int num : numbers) {
            System.out.println("     " + num + " * 2 = " + (num * 2));
        }
        
        // Function calls
        System.out.println("\n3. Function Calls:");
        System.out.println("   Fibonacci sequence (first 10 numbers):");
        for (int i = 0; i < 10; i++) {
            System.out.println("     F(" + i + ") = " + fibonacci(i));
        }
        
        // String operations
        System.out.println("\n4. String Operations:");
        String message = "Hello, World!";
        System.out.println("   Original: '" + message + "'");
        System.out.println("   Uppercase: '" + message.toUpperCase() + "'");
        System.out.println("   Lowercase: '" + message.toLowerCase() + "'");
        System.out.println("   Length: " + message.length() + " characters");
        
        // Object-oriented features
        System.out.println("\n5. Object-Oriented Features:");
        Person person = new Person("Java Developer", 30);
        person.addSkill("Java");
        person.addSkill("Spring");
        person.addSkill("Docker");
        System.out.println("   Person: " + person);
        System.out.println("   Name: " + person.getName());
        System.out.println("   Skills: " + person.getSkillsAsString());
        
        System.out.println("\n========================================");
        System.out.println("✅ Java execution completed successfully!");
    }
}

/**
 * Simple Person class to demonstrate OOP
 */
class Person {
    private String name;
    private int age;
    private java.util.List<String> skills;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        this.skills = new java.util.ArrayList<>();
    }
    
    public void addSkill(String skill) {
        skills.add(skill);
    }
    
    public String getName() {
        return name;
    }
    
    public String getSkillsAsString() {
        return String.join(", ", skills);
    }
    
    @Override
    public String toString() {
        return "Person{name='" + name + "', age=" + age + ", skills=" + skills + "}";
    }
} 