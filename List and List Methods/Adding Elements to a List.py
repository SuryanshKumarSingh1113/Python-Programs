                                 #Adding elements in a list

# append()
# Adds an element to the end of the list.

items = ["apple", "banana"]
items.append("orange")
print(items)


# insert()
# Inserts an element at a specific index.

items = ["apple", "banana"]
items.insert(1, "orange")
print(items)


# extend()
# Adds multiple elements from another list.

items = ["apple", "banana"]
more_items = ["orange", "mango"]
items.extend(more_items)
print(items)


#concatenate()
#Adds the elements of two lists

items = ["apple", "banana"]
more_items = ["orange", "mango"]
fruits = items+more_items
print(fruits)
