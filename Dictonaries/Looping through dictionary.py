                                                # Looping Through a Dictionary
student = {"name":"Prajwal","dept":"AIML","roll no":34,"college":"RYMEC"}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key value pairs
for key, value in student.items():
    print(key, value)


# Checking for Keys
# Use the in keyword to check if a key exists.

print("name" in student)    #returns true
print("gender" in student)  #returns false
