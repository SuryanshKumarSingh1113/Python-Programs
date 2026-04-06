                                                # Tuple & Tuple Methods in Python

# Tuples are used to store multiple values in a single variable, similar to lists.
# The key difference is that tuples are immutable, which means their values cannot be changed after creation.
# Tuples are commonly used when the data should remain constant.
# Tuples have fewer built in methods compared to lists.

# When to Use Tuples:

# When data should not change
# When you want to protect values from modification
# When returning multiple values from a function


# Summary

# Tuples store multiple values like lists
# Tuples are immutable and cannot be modified
# They support indexing, slicing, and looping
# Tuples have only two built in methods: count() and index()
# Tuple packing and unpacking make code clean and readable


# Creating a Tuple
# Tuples are created using parentheses ().

numbers = (1, 2, 3)
names = ("Alice", "Bob", "Charlie")
mixed = (1, "Python", 3.5, True)
print(numbers)
print(names)

# Single Element Tuple
# A tuple with one element must include a trailing comma.Without the comma, Python will treat it as a normal value.

single = (5,)
print(single)

# Accessing Tuple Elements
# Tuples elements are accessed using indexes.Indexing starts from 0.

items = ("apple", "banana", "orange")
 
print(items[0])
print(items[2])


# Use the len() function to get the number of elements in a tuple.

items = ("apple", "banana", "orange")
count = len(items)
print(count)
print(len(items))


# Tuples are Immutable
# Tuples cannot be modified after creation.This will cause an error.

items = ("apple", "banana", "orange")
items[1] = "grapes"





