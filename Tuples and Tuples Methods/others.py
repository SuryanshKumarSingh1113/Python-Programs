# Converting Between List and Tuple
# You can convert a tuple to a list and vice versa.

items = ("apple", "banana")
items_list = list(items)
print(items_list)
print(list(items))
 
items_tuple = tuple(items_list)
print(items_tuple)


# Looping Through a Tuple
# You can loop through tuple elements using a for loop.

items = ("apple", "banana", "orange")
 
for item in items:
    print(item)