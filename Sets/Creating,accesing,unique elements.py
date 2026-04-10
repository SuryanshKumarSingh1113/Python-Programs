                                                        # Sets in Python

# Sets are used to store multiple values in a single variable.
# A set does not allow duplicate values and does not maintain any specific order.
# Sets are commonly used when you want unique elements.
# Sets do not maintain order
# Sets do not support indexing
# Elements in a set must be immutable



# Creating a Set

# Sets are created using curly braces {} or the set() function.

numbers = {1, 2, 3, 4}                         #numbers = set([1,2,3,4])
names = {"Alice", "Bob", "Charlie"}
print(numbers)


# To create an empty set, use set().

# Using {} creates an empty dictionary, not a set.

empty_set = set()
print(empty_set)


# Unique Elements in a Set

# Sets automatically remove duplicate values.

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)



# Accessing Set Elements

# Sets do not support indexing or slicing because they are unordered.
# To access elements, you must loop through the set.

items = {"apple", "banana", "orange"}
 
for item in items:
    print(item)


#length of a set
hobby = {"cricket","football","traveling"}  
print(len(hobby))