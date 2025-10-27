# Python Basics: Binary Conversion

## Project Overview

This project is a Python program designed to practice foundational programming skills including input validation, data type conversion, message handling, and modular code structure. The program interacts with the user to collect and validate input, process and format the data, and then display personalized messages gracefully.

## Features

Input Validation: Ensures user inputs are not empty and correctly formatted.

Data Conversion: Converts string inputs to integers safely with error handling.

Message Handling: Writes, reads, and displays user messages with appropriate formatting.

Modular Design: Uses functions to separate concerns and make the program easier to read and maintain.

User Interaction: Displays personalized greetings and thank you messages to the user.

## Functions
### 1. collect_input(prompt)

Prompts the user for input.

Validates that the input is a non-empty string.

Returns the validated string input.

### 2. convert_to_int(input_str)

Attempts to convert a string to an integer.

Handles conversion errors gracefully.

Returns the integer or raises an appropriate message if conversion fails.

### 3. write_message(filename, message)

Writes the provided message to a specified file.

Confirms successful writing.

### 4. read_message(filename)

Reads the message from the specified file.

Returns the content of the file as a string.

### 5. display_message(message)

Prints the message to the console in a formatted way.

### How to Run

''' Run the Python program.

The program will prompt you to enter your name and age.

It will validate the inputs and store the age as an integer.

The program will then ask you to enter a message.

Your message will be saved to a file and read back.

Finally, the program will display a greeting and thank you message.
'''

### Example Interaction
Enter your name: Alice
Enter your age: 30
Enter your message: Hello, this is a test message.

Welcome Alice!
Your age is 30 years old.
Your message has been saved and read successfully.
Thank you for using the program, Alice!

### Learning Objectives

Apply core Python programming concepts including input validation, error handling, file operations, and functions.

Build modular and interactive programs with clear separation of concerns.

Practice handling user input and data conversion in Python.

Demonstrate proficiency in reading from and writing to files.
