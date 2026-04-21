# Lambda Functions
# Lambda functions are small anonymous functions written in one line.

add = lambda a, b: a + b
print(add(3, 5))


# Scope of Variables
# Variables defined inside a function are local to that function.
x=20
def test():
    x = 10
    print(x)
test() 
print(x)   

# Variables defined outside functions are global.