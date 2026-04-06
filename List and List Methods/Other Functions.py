# Copying Lists

# copy()
# Creates a shallow copy of the list.

items = ["apple", "banana"]
new_items = items.copy()
new_items.append("mango")
print (new_items)



# Checking Membership
# Use the in keyword to check if an element exists in a list.

items = ["apple", "banana", "orange"]
print("apple" in items)
items.pop(0)
print("apple" in items)


# Modifying List Elements
# Lists are mutable, which means their values can be changed.

items = ["apple", "banana", "orange"]
items[1] = "grapes"
print(items)


# Negative Indexing
# Negative indexes start from the end of the list.

items = ["apple", "banana", "orange"]
 
print(items[-1])
print(items[-2])


# List Slicing
# Slicing is used to extract part of a list.

items = ["apple", "banana", "orange", "mango"]
 
print(items[1:3])            #index 3 is not included
print(items[:2])
print(items[2:])




# Summary


# Lists store multiple values in one variable
# They support indexing, slicing, and negative indexing
# Lists are mutable and can be modified
# Python provides many built in list methods for adding, removing, and sorting elements
# Lists are widely used in everyday Python programming
