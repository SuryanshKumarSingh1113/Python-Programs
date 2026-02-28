#Accessing Characters in a String
# Strings are indexed, which means each character has a position.

name = "Shruthi singh"
print(name[0])
print(name[1])
print(name[7])



# String Slicing
# Slicing is used to extract a portion of a string.

print(name[0:7])      #0 is the starting index thats inclusive whereas 7 is the ending index and thats exclusive
print(name[0:6])
print('Shruthi last name is '+ name[8:15])

# When slicing a string with negative indexes, Python internally adds the length of the string to the negative value.

print(name[-5:])
print(name[-13:])
print(name[6-5:6-2])