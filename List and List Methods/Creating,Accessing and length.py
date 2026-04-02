                                             #List & List Methods in Python
# Lists are used to store multiple values in a single variable.
# They are one of the most flexible and commonly used data structures in Python.
# A list can store different types of data and can be modified after creation(ie They are mutable)

#creating a list:-
# Lists are created using square brackets []

fruits=["apple,mango,banana"]                  #in this line "apple,banana,grapes" its treated as a single element
fruits2=["apple","banana","grapes"]            #in this line "apple","banana","grapes" its treated as a 3 different elements
numbers = [1,2,3,4]
mixed=[1,2,"mango","apple",5]
print(fruits)
print(fruits2)
print(numbers)
print(mixed)
print(type(fruits))

# Accessing List Elements
# List elements are accessed using indexes.Indexing starts from 0.

print(fruits[0])
print(fruits2[2])
print(numbers[1])
print(mixed[2])

# List Length
# Use the len() function to get the number of elements in a list.

print(len(fruits))
print(len(fruits2))
print(len(mixed))
count = len(numbers)
print(count)