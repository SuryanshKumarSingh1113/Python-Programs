                                        # Removing Elements from a List

# remove()
# Removes the first occurrence of a value.

items = ["apple", "banana", "orange"]
items.remove("banana")
print(items)


# pop()
# Removes and returns an element at a given index. If no index is provided, it removes the last element.

items = ["apple", "banana", "orange"]
items.pop()
print(items)
items2 = ["apple", "banana", "orange"]
items.pop(0)
print(items2)


# clear()
# Removes all elements from the list.

items = ["apple", "banana"]
items.clear()
print(items)

