def greet(name):
    print("Hello",name)

# greet()                      #here parameter(name) is not passed so it gives an error
greet("rohan")               #here argument(rohan) is passed so it doesn't gives an error


# Default Parameter Values
# You can provide default values to parameters.

def greet(name="User"):
    print("Hello", name)
 
greet()                             #here parameter(name) is passed by default so it doesn't gives an error
greet("Harry")

# Keyword Arguments
# Arguments can be passed using parameter names.

def user_info(name, age):
    print("hello", name, "you are",age ,"years old")
 
user_info(25,"rohan")                        
user_info(age=25, name="Harry")


# Function Inside a Function
# Functions can be defined inside other functions.

def outer():
    def inner():
        print("Inside inner function")
    inner()                                 #it should be inside outer()

        
outer()

