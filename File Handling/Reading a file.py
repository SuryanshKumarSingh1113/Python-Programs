# Reading a File
# read()
# Reads the entire file content as a string.

f = open("data.txt", "r")        
content = f.read()
print(content)
f.close()

# readline()
# Reads one line at a time.

f = open("data.txt", "r")
line = f.readline()
print(line)
f.close()

# readlines()
# Reads all lines and returns them as a list.

f = open("data.txt", "r")
lines = f.readlines()
print(lines)
f.close()