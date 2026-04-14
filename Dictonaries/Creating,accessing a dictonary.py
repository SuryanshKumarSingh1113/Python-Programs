                                                    # Dictionaries in Python
# Dictionaries are used to store data in key-value pairs.
# Each key is linked to a value, making dictionaries ideal for structured data.
# Dictionaries are one of the most important data structures in Python.
# Keys must be unique
# Keys must be immutable
# Values can be of any data type
# Dictionaries are mutable


# Creating a Dictionary
# Dictionaries are created using curly braces {} with key-value pairs separated by colons.

student = {
    "name": "Harry",
    "age": 25,
    "city": "Delhi"
}

# You can also create a dictionary using the dict() function.

student = dict(name="Harry", age=25, city="Delhi")

# Accessing Dictionary Values
# Values are accessed using keys.
# Using a key that does not exist will cause an error.

print(student["name"])
print(student["age"])


# Using get()
# The get() method safely retrieves a value.
# If the key does not exist, None is returned instead of an error.

print(student.get("city"))
print(student.get("email"))




