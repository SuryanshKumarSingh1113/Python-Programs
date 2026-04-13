                                                    # Adding Elements to a Set

# add()
# Adds a single element to the set.

items = {"apple", "banana"}
items.add("orange")
print(items)

# update()
# Adds multiple elements from another iterable.

items = {"apple", "banana"}
items.update(["orange", "mango"])
print (items)


# Sets are Mutable
# Sets can be modified after creation.

items = {"apple", "banana"}
items.add("strawberry")
print(items)