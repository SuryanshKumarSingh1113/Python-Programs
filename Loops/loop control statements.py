# Loop Control Statements
# Python provides special statements to control loop execution.

# break
# Stops the loop completely.

for i in range(10):
    if i == 5:                #it prints from 0 to 4
        break
    print(i)

# continue
# Skips the current iteration and moves to the next one.

for i in range(5):                    #it prints from 0 to 4 except 2
    if i == 2:
        continue
    print(i)

# pass
# Acts as a placeholder where a statement is required.

for i in range(5):
    pass

