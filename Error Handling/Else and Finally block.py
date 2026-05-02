# The else Block
# The else block runs if no error occurs.

try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("Conversion successful")

# The finally Block
# The finally block always runs, whether an error occurs or not.

try:
    file = open("data5.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")

