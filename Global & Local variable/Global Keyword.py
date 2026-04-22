# The global Keyword
# The global keyword is used to modify a global variable inside a function.

x = 10
 
def update():
    global x
    x = 20
 
update()
print(x)

# Without the global keyword, Python treats x as a local variable.

# Why global Should Be Used Carefully

# Using global variables can make code harder to understand and debug.
# It is generally better to:
# Pass values as parameters
# Return values from functions


# Global Variables and Function Parameters
# A better approach than using global is passing data explicitly.

def update(x):
    return x + 10
 
value = 5
value = update(value)
print(value)

# Variable Scope Rules
# Local variables exist only inside functions
# Global variables exist throughout the program
# Local variables override global variables with the same name
# The global keyword allows modifying global variables