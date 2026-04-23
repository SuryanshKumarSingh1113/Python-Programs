# Local vs Global Example
x = 10
 
def test():
    x = 5
    print(x)
 
test()
print(x)

# Output:

# Inside function: 5
# Outside function: 10
# The local variable does not affect the global variable.