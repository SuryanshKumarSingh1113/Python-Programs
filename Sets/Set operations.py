                                                        # Set Operations
# Sets support mathematical set operations.

# Union
# Combines elements from both sets.

a = {1, 2, 3}
b = {3, 4, 5}
 
result = a.union(b)
print(result)

# Intersection
# Returns common elements between sets.

result = a.intersection(b)
print(result)

# Difference
# Returns elements present in the first set but not in the second.

result = a.difference(b)
print(result)

# Symmetric Difference
# Returns elements present in either set but not in both.

result = a.symmetric_difference(b)
print(result)

# Membership Testing
# Use the in keyword to check if an element exists in a set.

print(10 in a)
 
items = {"apple", "banana", "orange"}
print ("banana" in items)