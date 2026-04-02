# replace()
# Replaces part of a string with another string.

address= 'Delhi chandani chowk'
print(address.replace('chandani',"gandhi"))


# split()
# Splits a string into a list based on a separator.

activity="football.hockey.cricket.tennis"
sports=activity.split('.')
print(sports)


# join()
# Joins elements of a list into a single string.

list=["cricket,football,volleyball,tennis"]
sports=",".join(list)
print(sports)


# strip()
# Removes extra spaces from the beginning and end of a string.

text = "  hello  "
print(text.strip())



# startswith() and endswith()
# Checks whether a string starts or ends with a given value.

email = "test@gmail.com"
 
print(email.startswith("test"))
print(email.endswith(".com"))


# String Concatenation
# Strings can be combined using the + operator.

first_name = "Suryansh"
second_name= "Singh"
 
result = first_name + " kumar " + second_name
print(result)


