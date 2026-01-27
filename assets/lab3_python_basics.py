"""
Lab 3: Python Basics, Files, and Functions
Introduction to Software Systems - IIIT Hyderabad

This document serves as an interactive lecture note for Laboratory 3. 
It covers the fundamental concepts of the Python programming language, 
file handling, and function definitions.

Topics Covered:
1.  Package Management with uv
2.  Input/Output Operations
3.  Variables and Data Types
4.  Operators
5.  Conditional Statements
6.  Loops
7.  Data Structures
8.  String Manipulation
9.  Functions
10. File Operations

Estimated Duration: 1.5 hours
"""

from edtrace import text
import os

def main():
    """Main entry point for the lab lecture."""
    introduction()
    section_uv_package_manager()
    section_basic_io()
    section_variables_and_types()
    section_operators()
    section_conditionals()
    section_loops()
    section_data_structures()
    section_strings()
    section_functions()
    section_files()
    conclusion()

# ============================================================================
# SECTION: Introduction
# ============================================================================

def introduction():
    text("# Lab 3: Python Basics, Files, and Functions")  # @hide
    text("### Introduction to Software Systems - IIIT Hyderabad")  # @hide
    text("")  # @hide
    text("Welcome to Lab 3. In this session, we will establish a foundational understanding of the Python programming language.")  # @hide
    text("Python is a high-level, interpreted programming language known for its readability and versatility. It is widely used in various domains, including web development, data science, artificial intelligence, and automation.")  # @hide
    text("")  # @hide
    text("### Learning Objectives")  # @hide
    text("By the end of this lab, you should be able to:")  # @hide
    text("1.  **Manage Projects**: Understand the utility of `uv` for dependency and project management.")  # @hide
    text("2.  **Use Core Syntax**: Correctly use variables, data types, and operators.")  # @hide
    text("3.  **Control Flow**: Implement conditional logic and iteration using loops.")  # @hide
    text("4.  **Organize Data**: Use data structures such as lists and dictionaries.")  # @hide
    text("5.  **Modularize Code**: Define and invoke functions to create reusable code blocks.")  # @hide
    text("6.  **Handle Files**: Read from and write to the file system.")  # @hide
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: uv Package Manager
# ============================================================================

def section_uv_package_manager():
    text("# Part 1: The uv Package Manager")  # @hide
    text("")  # @hide
    text("Modern software development requires robust tools for managing dependencies and environments. For this course, we utilize **uv**, a high-performance Python package and project manager written in Rust.")  # @hide 
    text("It serves as a unified replacement for traditional tools such as `pip`, `pip-tools`, and `virtualenv`, offering significantly faster execution times.")  # @hide
    text("")  # @hide
    
    text("## Key Commands")  # @hide
    text("The following commands are essential for managing your Python projects:")  # @hide
    text("")  # @hide
    
    text("### 1. Initialize a Project")  # @hide
    text("To initialize a new project, use the `init` command. This generates a `pyproject.toml` file, which is the standard configuration file for Python projects.")  # @hide
    text("```bash\nuv init [project_name]\n```", verbatim=True)  # @hide
    text("If executed within an existing directory without a project name, it initializes the project in the current working directory.")  # @hide
    text("")  # @hide

    text("### 2. Add Packages")  # @hide
    text("External libraries are essential for extending Python's capabilities. To install a library, such as `requests` for making HTTP requests, use the `add` command:")  # @hide
    text("```bash\nuv add requests\n```", verbatim=True)  # @hide
    text("This command automatically updates the `pyproject.toml` file to include the dependency and resolves the version constraints in the `uv.lock` file.")  # @hide
    text("")  # @hide

    text("### 3. Remove Packages")  # @hide
    text("To remove an unnecessary library from your project dependencies:")  # @hide
    text("```bash\nuv remove requests\n```", verbatim=True)  # @hide
    text("")  # @hide

    text("### 4. Run Scripts")  # @hide
    text("To execute a Python script within the context of the project's virtual environment, use the `run` command. This ensures that the script has access to the installed dependencies.")  # @hide
    text("```bash\nuv run python script.py\n```", verbatim=True)  # @hide
    text("Alternatively, you can run specific tools or modules:")  # @hide
    text("```bash\nuv run pytest\n```", verbatim=True)  # @hide
    text("")  # @hide
    
    text("### Hands-On Exercise 1: Project Setup")  # @hide
    text("1. Open your terminal.")  # @hide
    text("2. Create a new directory named `lab3_exercise` and navigate into it.")  # @hide
    text("3. Run `uv init` to initialize the project.")  # @hide
    text("4. Inspect the generated `pyproject.toml` file.")  # @hide
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Basic I/O
# ============================================================================

def section_basic_io():
    text("# Part 2: Basic Input/Output (I/O)")  # @hide
    text("")  # @hide
    text("Input and Output (I/O) operations allow a program to interact with the external world, primarily through the console in this context.")  # @hide
    
    text("## Output: The `print()` Function")  # @hide
    text("The `print()` function is used to display output to the standard output device (console).")  # @hide
    
    print("Hello, World!")
    text("Hello, World!", verbatim=True)  # @hide
    
    name = "Student" # @inspect name
    print("Welcome,", name)
    text("Welcome, Student", verbatim=True)  # @hide
    
    text("### Formatted String Literals (f-strings)")  # @hide
    text("Introduced in Python 3.6, f-strings provide a concise and readable way to embed expressions inside string literals. An f-string is prefixed with the letter `f`.")  # @hide
    
    language = "Python" # @inspect language
    version = 3.12 # @inspect version
    
    # The expressions inside the curly braces {} are evaluated at runtime.
    message = f"We are learning {language} version {version}." # @inspect message
    print(message)
    text("We are learning Python version 3.12.", verbatim=True)  # @hide
    
    text("")  # @hide
    text("## Input: The `input()` Function")  # @hide
    text("The `input()` function pauses program execution to wait for the user to type text and press Enter. It returns the entered data as a **string**.")  # @hide
    
    text("```python", verbatim=True)  # @hide
    text('user_name = input("Enter your name: ")', verbatim=True)  # @hide
    text('print(f"Greeting, {user_name}.")', verbatim=True)  # @hide
    text("```", verbatim=True)  # @hide
    
    text("### Type Conversion")  # @hide
    text("Since `input()` always returns a string, mathematical operations on the input require explicit type conversion.")  # @hide
    text("```python", verbatim=True)  # @hide
    text('age_str = input("Enter your age: ")', verbatim=True)  # @hide
    text('age = int(age_str)  # Convert the string to an integer', verbatim=True)  # @hide
    text("```", verbatim=True)  # @hide
    text("")  # @hide

    text("### Hands-On Exercise 2: Interactive Greeting")  # @hide
    text("Create a Python script that:")  # @hide
    text("1. Prompts the user for their favorite color.")  # @hide
    text("2. Prompts the user for their birth year.")  # @hide
    text("3. Calculates their approximate age.")  # @hide
    text("4. Prints a message using the color and age.")  # @hide
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Variables and Types
# ============================================================================

def section_variables_and_types():
    text("# Part 3: Variables and Data Types")  # @hide
    text("")  # @hide
    text("A variable in Python is a symbolic name that is a reference or pointer to an object. Unlike statically typed languages, you do not need to declare the type of a variable before using it.")  # @hide
    
    text("## Fundamental Data Types")  # @hide
    
    # Integer (int): Represents whole numbers.
    items = 10 # @inspect items
    
    # Floating Point (float): Represents real numbers with decimal points.
    price = 19.99 # @inspect price
    
    # String (str): Represents a sequence of characters.
    brand = "Acme Corp" # @inspect brand
    
    # Boolean (bool): Represents truth values, True or False.
    is_available = True # @inspect is_available
    
    # NoneType (None): Represents the absence of a value or a null value.
    discount = None # @inspect discount
    
    text("The `type()` function returns the class type of the argument passed.")  # @hide
    print(f"Type of items: {type(items)}")
    text("Type of items: <class 'int'>", verbatim=True)  # @hide
    print(f"Type of price: {type(price)}")
    text("Type of price: <class 'float'>", verbatim=True)  # @hide
    
    text("")  # @hide
    text("## Dynamic Typing")  # @hide
    text("Python is dynamically typed, meaning the type of a variable is determined at runtime and can change during execution.")  # @hide
    
    x = 100 # @inspect x
    text(f"x is initially an integer: {x}", verbatim=True) # @hide
    x = "Now I am a string" # @inspect x
    text(f"x is now a string: {x}", verbatim=True) # @hide
    
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Operators
# ============================================================================

def section_operators():
    text("# Part 4: Operators")  # @hide
    text("")  # @hide
    
    text("## Arithmetic Operators")  # @hide
    text("Python supports standard arithmetic operations.") # @hide
    a, b = 10, 3 # @inspect a b
    
    print(f"{a} + {b} = {a + b}")      # Addition
    text("10 + 3 = 13", verbatim=True)  # @hide
    print(f"{a} - {b} = {a - b}")      # Subtraction
    text("10 - 3 = 7", verbatim=True)  # @hide
    print(f"{a} * {b} = {a * b}")      # Multiplication
    text("10 * 3 = 30", verbatim=True)  # @hide
    print(f"{a} / {b} = {a / b}")      # True Division (returns float)
    text("10 / 3 = 3.3333333333333335", verbatim=True)  # @hide
    print(f"{a} // {b} = {a // b}")    # Floor Division (returns integer quotient)
    text("10 // 3 = 3", verbatim=True)  # @hide
    print(f"{a} % {b} = {a % b}")      # Modulo (returns remainder)
    text("10 % 3 = 1", verbatim=True)  # @hide
    print(f"{a} ** {b} = {a ** b}")    # Exponentiation (power)
    text("10 ** 3 = 1000", verbatim=True)  # @hide
    
    text("")  # @hide
    text("## Logical and Comparison Operators")  # @hide
    
    is_adult = True # @inspect is_adult
    has_ticket = False # @inspect has_ticket
    
    # Logical AND: Returns True if both operands are True
    can_enter = is_adult and has_ticket # @inspect can_enter
    print(f"Can enter? {can_enter}")
    text("Can enter? False", verbatim=True)  # @hide
    
    # Comparison Operators
    print(f"10 > 3: {10 > 3}")
    text("10 > 3: True", verbatim=True)  # @hide
    print(f"10 == 10: {10 == 10}")
    text("10 == 10: True", verbatim=True)  # @hide
    print(f"10 != 5: {10 != 5}")
    text("10 != 5: True", verbatim=True)  # @hide
    
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Conditionals
# ============================================================================

def section_conditionals():
    text("# Part 5: Conditional Statements")  # @hide
    text("")  # @hide
    text("Conditional statements allow a program to execute different separate blocks of code based on strict conditions.")  # @hide
    
    battery_level = 15 # @inspect battery_level
    
    # The if-elif-else structure
    if battery_level > 80:
        status = "Healthy"
    elif battery_level > 20:
        status = "Okay"
    else:
        status = "Low Battery"
        
    print(f"Battery Status: {status}")
    text("Battery Status: Low Battery", verbatim=True)  # @hide
    
    text("")  # @hide
    text("### Indentation")  # @hide
    text("It is critical to note that Python uses **indentation** (whitespace) to define the scope of code blocks, such as loops, functions, and classes. Standard practice is to use 4 spaces per indentation level.")  # @hide
    
    text("")  # @hide
    text("### Hands-On Exercise 3: Grade Calculator")  # @hide
    text("Write a program that:")  # @hide
    text("1. Asks the user for a numerical score (0-100).")  # @hide
    text("2. Prints 'Pass' if the score is 50 or above.")  # @hide
    text("3. Prints 'Fail' if the score is below 50.")  # @hide
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Loops
# ============================================================================

def section_loops():
    text("# Part 6: Loops")  # @hide
    text("")  # @hide
    text("Loops are used to iterate over a sequence or logical condition, allowing code to be executed repeatedly.")  # @hide
    
    text("## The `for` Loop")  # @hide
    text("The `for` loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string).")  # @hide
    
    text("Example: Iterating through a range of numbers:")  # @hide
    # range(5) generates numbers from 0 to 4
    for i in range(5): # @inspect i
        print(f"Index: {i}", end=" ")
    print() # Newline
    text("Index: 0 Index: 1 Index: 2 Index: 3 Index: 4 ", verbatim=True)  # @hide
    
    text("")  # @hide
    text("## The `while` Loop")  # @hide
    text("The `while` loop executes a set of statements as long as a condition is true.")  # @hide
    
    countdown = 3 # @inspect countdown
    while countdown > 0: # @inspect countdown
        print(f"{countdown}...")
        text(f"{countdown}...", verbatim=True)  # @hide
        countdown -= 1
    print("Liftoff.")
    text("Liftoff.", verbatim=True)  # @hide
    
    text("")  # @hide
    text("### Hands-On Exercise 4: Countdown")  # @hide
    text("Write a loop that prints all even numbers from 10 down to 0.")  # @hide
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Data Structures
# ============================================================================

def section_data_structures():
    text("# Part 7: Data Structures")  # @hide
    text("Efficient data organization is crucial for software performance. Python provides several built-in data structures.")  # @hide
    text("")  # @hide
    
    text("## 1. Lists")  # @hide
    text("A list is an ordered, mutable collection of items. Lists are defined using square brackets `[]`.")  # @hide
    
    tasks = ["Analyze requirements", "Design system", "Implement code"] # @inspect tasks
    
    # Accessing elements by index (0-based)
    first_task = tasks[0] # @inspect first_task
    
    # Modifying the list
    tasks.append("Deploy") # Adds a new item to the end @inspect tasks
    tasks[1] = "Refine architecture" # Modifies the item at index 1 @inspect tasks
    
    print(f"Tasks: {tasks}")
    text(f"Tasks: {tasks}", verbatim=True)  # @hide
    
    text("")  # @hide
    text("## List Slicing")  # @hide
    text("Slicing allows you to extract a portion of a list using the syntax `list[start:stop:step]`.")  # @hide
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # @inspect numbers
    
    # Basic slicing: list[start:stop] - extracts elements from start to stop-1
    first_three = numbers[0:3] # @inspect first_three
    print(f"First three: {first_three}")
    text("First three: [0, 1, 2]", verbatim=True)  # @hide
    
    # Omitting start defaults to 0, omitting stop defaults to end
    last_four = numbers[-4:] # @inspect last_four
    print(f"Last four: {last_four}")
    text("Last four: [6, 7, 8, 9]", verbatim=True)  # @hide
    
    # Using step to skip elements
    every_second = numbers[::2] # @inspect every_second
    print(f"Every second element: {every_second}")
    text("Every second element: [0, 2, 4, 6, 8]", verbatim=True)  # @hide
    
    # Reverse a list using negative step
    reversed_list = numbers[::-1] # @inspect reversed_list
    print(f"Reversed: {reversed_list}")
    text("Reversed: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]", verbatim=True)  # @hide
    
    # Extracting a middle portion
    middle = numbers[3:7] # @inspect middle
    print(f"Middle portion (index 3-6): {middle}")
    text("Middle portion (index 3-6): [3, 4, 5, 6]", verbatim=True)  # @hide
    
    text("")  # @hide
    text("## 2. Strings")  # @hide
    text("Strings are immutable sequences of Unicode characters.")  # @hide
    
    language = "Python" # @inspect language
    print(f"First character: {language[0]}")
    text(f"First character: {language[0]}", verbatim=True)  # @hide
    print(f"Last character: {language[-1]}")
    text(f"Last character: {language[-1]}", verbatim=True)  # @hide
    
    text("")  # @hide
    text("## 3. Dictionaries")  # @hide
    text("A dictionary is an unordered collection of data values, used to store data values like a map. Dictionaries hold key-value pairs.")  # @hide
    
    user_profile = {
        "username": "student_01",
        "role": "Administrator",
        "access_level": 5
    } # @inspect user_profile
    
    print(f"User: {user_profile['username']}")
    text(f"User: {user_profile['username']}", verbatim=True)  # @hide
    print(f"Role: {user_profile['role']}")
    text(f"Role: {user_profile['role']}", verbatim=True)  # @hide
    
    # Adding a new key-value pair
    user_profile["active"] = True # @inspect user_profile
    
    text("")  # @hide
    text("### Hands-On Exercise 5: Shopping List")  # @hide
    text("1. Create a Python list containing three grocery items.")  # @hide
    text("2. Add a fourth item to the list.")  # @hide
    text("3. Print the second item in the list.")  # @hide
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Strings
# ============================================================================

def section_strings():
    text("# Part 8: String Manipulation")  # @hide
    text("Python includes a rich set of methods for processing strings.")  # @hide
    text("")  # @hide
    
    raw_text = "   Data Processing   " # @inspect raw_text
    
    # The strip() method removes leading and trailing whitespace.
    clean_text = raw_text.strip() # @inspect clean_text
    
    # Text case transformations
    print(clean_text.upper())
    text("DATA PROCESSING", verbatim=True)  # @hide
    print(clean_text.lower())
    text("data processing", verbatim=True)  # @hide
    
    # The split() method splits a string into a list where each word is a list item.
    words = clean_text.split() # @inspect words
    print(f"Words: {words}")
    text(f"Words: {words}", verbatim=True)  # @hide
    
    # The join() method combines all items in an iterable into a string.
    sentence = "-".join(words) # @inspect sentence
    print(f"Joined: {sentence}")
    text(f"Joined: {sentence}", verbatim=True)  # @hide
    
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Functions
# ============================================================================

def section_functions():
    text("# Part 9: Functions")  # @hide
    text("Functions are reusable blocks of code that perform a specific task. They help in utilizing the concept of code modularity.")  # @hide
    
    text("## Defining a Function")  # @hide
    
    # Functions are defined using the 'def' keyword.
    def generate_greeting(name, specific_greeting="Hello"):
        """
        Generates a greeting message.
        
        Args:
            name (str): The name of the person.
            specific_greeting (str): The greeting to use. Defaults to "Hello".
            
        Returns:
            str: The formatted greeting string.
        """
        message = f"{specific_greeting}, {name}."
        return message

    # Invoking the function
    msg1 = generate_greeting("Alice") # @inspect msg1
    msg2 = generate_greeting("Bob", "Greetings") # @inspect msg2
    
    print(msg1)
    text(msg1, verbatim=True)  # @hide
    print(msg2)
    text(msg2, verbatim=True)  # @hide
    
    text("")  # @hide
    text("## Return Rules")  # @hide
    text("A function can return a value using the `return` statement. If no return statement is specified, the function returns `None` by default.")  # @hide
    
    def calculate_square(n):
        return n * n
        
    result = calculate_square(5) # @inspect result
    print(f"The square of 5 is {result}")
    text(f"The square of 5 is {result}", verbatim=True)  # @hide
    
    text("")  # @hide
    text("## Recursion")  # @hide
    text("Recursion is a programming technique where a function calls itself to solve a problem. A recursive function must have a **base case** (a condition that stops the recursion) and a **recursive case** (where the function calls itself with a modified argument).")  # @hide
    
    text("")  # @hide
    text("### Example 1: Factorial")  # @hide
    text("The factorial of a non-negative integer n (denoted as n!) is the product of all positive integers less than or equal to n.")  # @hide
    
    def factorial(n):
        """
        Calculates the factorial of a non-negative integer recursively.
        
        Args:
            n (int): A non-negative integer.
            
        Returns:
            int: The factorial of n.
        """
        # Base case: factorial of 0 or 1 is 1
        if n <= 1:
            return 1
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)
    
    fact_5 = factorial(5) # @inspect fact_5
    print(f"5! = {fact_5}")
    text("5! = 120", verbatim=True)  # @hide
    
    text("")  # @hide
    text("### Example 2: Fibonacci Sequence")  # @hide
    text("The Fibonacci sequence is a series where each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, ...")  # @hide
    
    def fibonacci(n):
        """
        Returns the nth Fibonacci number using recursion.
        
        Args:
            n (int): The position in the Fibonacci sequence (0-indexed).
            
        Returns:
            int: The nth Fibonacci number.
        """
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    fib_7 = fibonacci(7) # @inspect fib_7
    print(f"The 7th Fibonacci number is {fib_7}")
    text("The 7th Fibonacci number is 13", verbatim=True)  # @hide
    
    # Generating a sequence of Fibonacci numbers
    fib_sequence = [fibonacci(i) for i in range(8)] # @inspect fib_sequence
    print(f"First 8 Fibonacci numbers: {fib_sequence}")
    text("First 8 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13]", verbatim=True)  # @hide
    
    text("")  # @hide
    text("### Important Considerations")  # @hide
    text("- **Base Case**: Always ensure a base case exists to prevent infinite recursion.")  # @hide
    text("- **Stack Depth**: Python has a default recursion limit (usually 1000). Deep recursion may cause a `RecursionError`.")  # @hide
    text("- **Efficiency**: Simple recursive solutions (like Fibonacci) can be inefficient due to repeated calculations. Consider memoization or iterative approaches for optimization.")  # @hide
    
    text("")  # @hide
    text("### Hands-On Exercise 6: Calculator Function")  # @hide
    text("Write a function called `multiply` that takes two arguments, calculates their product, and returns the result. Test it by calling it with two numbers.")  # @hide
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Files
# ============================================================================

def section_files():
    text("# Part 10: File Operations")  # @hide
    text("File handling allows programs to persist data on the storage system.")  # @hide
    text("")  # @hide
    
    filename = "lab3_log.txt" # @inspect filename
    
    text("## Writing to a File")  # @hide
    text("We use the `open()` function along with the `with` statement. The `with` statement is a context manager that ensures the file is properly closed after operations are complete, even if an exception occurs.")  # @hide
    
    with open(filename, "w") as f:
        f.write("System execution started.\n")
        f.write("Initialization complete.\n")
    
    text("File written successfully.")  # @hide
    
    text("")  # @hide
    text("## Reading from a File")  # @hide
    
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read() # @inspect content
            print("File Contents:")
            text("File Contents:", verbatim=True)  # @hide
            print(content)
            text(content, verbatim=True)  # @hide
            
    # Clean up the file after demonstration
    if os.path.exists(filename):
        os.remove(filename)
        text("(Demonstration file removed)")  # @hide

    text("")  # @hide
    text("### Hands-On Exercise 7: File Logger")  # @hide
    text("Write a script that asks the user for a sentence and appends it to a file named `my_journal.txt`. Ensure that each new entry opens on a new line.")  # @hide
    text("")  # @hide
    text("---")  # @hide

# ============================================================================
# SECTION: Conclusion
# ============================================================================

def conclusion():
    text("# Conclusion")  # @hide
    text("")  # @hide
    text("This laboratory session has covered the essential building blocks of Python programming.")  # @hide
    text("")  # @hide
    text("### Summary:")  # @hide
    text("- **Environment**: We learned to use `uv` for efficient project management.")  # @hide
    text("- **Syntax**: We explored variables, types, and operational logic.")  # @hide
    text("- **Structure**: We implemented control flows using conditionals and loops.")  # @hide
    text("- **Modularity**: We practiced writing functions and handling files.")  # @hide
    text("")  # @hide
    text("You successfully completed the hands-on exercises.")  # @hide

if __name__ == "__main__":
    main()
