# Using the with Statement
# The with statement automatically closes the file.
# This is the recommended way to work with files.

with open("data.txt", "r") as file:
    content = file.read()
    print(content)


with open("data2.txt", "r") as f:
    content = f.read()
    print(content)