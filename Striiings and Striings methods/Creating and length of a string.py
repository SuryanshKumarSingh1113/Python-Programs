                               #STRINGS
# Strings are used to store text data in Python.
# Any value written inside single quotes or double quotes is treated as a string.
# Strings are one of the most commonly used data types and Python provides many built in methods to work with them.



#Creating a String

name = "Shruthi Singh"    #Strings can be created using single quotes or double quotes
Hobby = 'Writing Poem'
Message = """I
love
 writing                       
 poems
 
"""                      #Multiline strings are created using triple quotes
print("My wife's name is",name,"Her hobby is",Hobby,Message)

#length of the string
print(len(name))


# find()
# Finds the position of a substring.Returns -1 if the value is not found.

position=name.find("ruthi")         #phle letter ka poisition btata h
print(position)


