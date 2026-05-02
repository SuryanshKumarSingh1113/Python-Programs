# Handling Specific Errors
# You can catch specific error types.

try:
    x = int("abc")
except ValueError:
    print("Invalid conversion")

# This helps in handling errors more precisely.