# Writing to a File
# Write Mode (w)
# Creates a new file or overwrites an existing file.

a="Hi my name is Suryansh"
file=open("data.txt","w")                     #even if a file is not there it creates a file and writes the content which is given
file.write(a)
file.close()

# Append Mode (a)
# Adds content to the end of a file.

file = open("data.txt", "a")               #'''if we use write mode instead of append then it creates a new file i.e the previous data is cleared
file.write("\nI'm learning python")
file.close()


#  Writing Multiple Lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
 
with open("data2.txt", "w") as file:
    file.writelines(lines)