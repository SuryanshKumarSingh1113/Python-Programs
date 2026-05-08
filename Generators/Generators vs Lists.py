# Generator vs List
# In Python, you can create generators using parentheses () instead of brackets []. Parenthesis are not tuple comprehensions, they create generators. List version:

numbers = [i for i in range(5)]
print(numbers)

# Generator version:

numbers2 = (i for i in range(5))
print(numbers2)

# Difference:
# List stores all values
# Generator produces values when needed
