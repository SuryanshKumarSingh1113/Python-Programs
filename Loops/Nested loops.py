# Nested Loops
# A loop inside another loop is called a nested loop.

for i in range(3):
    for j in range(2):
        print(i, j)


# Looping with else
# The else block runs when the loop finishes normally.

for i in range(3):
    print(i)
    
else:
    print("Loop finished")

# The else block does not run if the loop is terminated using break.