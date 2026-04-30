# Reading and Writing Binary Files
with open("data2.txt", "rb") as file:        #read binary(rb)
    data = file.read()
    print(data)

with open("copy.png", "wb") as file:         #write binary(wb)
    file.write(data)