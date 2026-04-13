                                            # Removing Elements from a Set
# remove()
# Removes a specified element. Raises an error if the element does not exist.

items = {"apple", "banana",'mango'}
items.remove("banana")
print(items)

# discard()
# Removes a specified element without raising an error.

items = {"apple", "banana"}
items.discard("grapes")
print(items)

# pop()
# Removes and returns a random element.

items = {"apple", "banana", "orange"}
items.pop()
print(items)

# clear()
# Removes all elements from the set.

items = {"apple", "banana"}
items.clear()
print(items)