# Raising Errors Manually
# You can raise an error using the raise keyword.

age = -5
 
if age < 0:
    raise ValueError("Age cannot be negative")



# Using pass in Error Handling
# The pass statement can be used when you want to ignore an error.

try:
    x = int("abc")
except ValueError:
    pass

# This is generally discouraged unless intentional.
