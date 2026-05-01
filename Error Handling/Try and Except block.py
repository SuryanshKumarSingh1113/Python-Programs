                                                # Error Handling in Python
# Errors are situations where a program cannot run as expected.
# Error handling allows a program to deal with such situations without crashing.
# Python uses try, except, else, and finally to handle errors.

# What is an Error?
# An error occurs when Python encounters a problem while executing code.

# Common examples:

# Dividing by zero
# Accessing a file that does not exist
# Converting invalid data types


# The try and except Block
# Code that may cause an error is placed inside the try block.
# If an error occurs, the code inside except runs.

try:
    x = int(input("Enter a no:"))
except:
    print("An error occurred")
print("thank you!!!")            # This line will be printed even if an error occurs




# Common Error Types
# Some common built in exceptions:

# ValueError
# TypeError
# ZeroDivisionError
# FileNotFoundError
# IndexError
# KeyError


# Why Error Handling is Important:-
# Prevents program crashes
# Makes programs more reliable
# Helps handle unexpected inputs
# Improves user experience