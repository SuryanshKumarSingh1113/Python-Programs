                                                    # Functions in Python
# Functions are used to group reusable code into a single block.
# They help make programs organized, readable, and easier to maintain.
# Instead of writing the same code again and again, you can define a function and reuse it whenever needed.


# Defining a Function
# Functions are defined using the def keyword.

def greet():
    print("Hello")

# Calling a Function
# To execute a function, you call it using its name followed by parentheses.

greet()


# Functions with Parameters
# Parameters allow you to pass data into a function.

def greet(name):
    print("Hello", name)
 
greet("Harry")

# Here, name is a parameter and "Harry" is an argument.


# Functions with Multiple Parameters
def add(a, b):
    print(a + b)
 
add(5, 3)

# Return Statement
# The return statement sends a value back from the function.

def add(a, b):
    return a + b             #return is used when a variable needs to have a value using that function
 
result = add(10, 5)     
print(result)                 

# Once return is executed, the function stops running.



# Function Docstrings
# Docstrings are used to describe what a function does.

def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b

product = multiply(5,21)
print(product)

