                                                        # Loops in Python
# Loops are used to execute a block of code multiple times.
# They help reduce repetition and make programs more efficient.
# Python mainly provides two types of loops:
# for loop
# while loop


# The for Loop
# The for loop is used to iterate over a sequence.

items = ["apple", "banana", "orange"]
 
for item in items:               # The loop runs once for each element in the sequence.
    print(item)



# Using range() with for Loop
# The range() function generates a sequence of numbers.

for i in range(5):                      # This will print numbers from 0 to 4.
    print(i)                          


# range() with Start and Step
for i in range(1, 10, 2):                 # This prints numbers from 1 to 9 with a step of 2.
    print(i)


# Looping Through a String
# Strings can also be iterated character by character.

text = "Python"
 
for char in text:
    print(char)