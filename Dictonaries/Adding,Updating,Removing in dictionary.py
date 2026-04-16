                                        # Adding and Updating Values
student={
    "name":"Vedant",
    "roll no":50,
    "college":"IIT Dholakpur"
}
print(student)

# You can add new key-value pairs or update existing ones.

student["email"] = "test@gmail.com"
student["roll no"] = 26
student["gender"]="male"
print(student)

# update()
# Adds multiple key value pairs at once.

student.update({
    "course": "Python",
    "level": "Beginner"
})
print(student)

                                         # Removing Dictionary Items

# pop()
# Removes a key and returns its value.

print(student.pop("roll no"))

# popitem()
# Removes and returns the last inserted key value pair.

print(student.popitem())

# del
# Deletes a key value pair.

del student["college"]
print(student)

# clear()
# Removes all items from the dictionary.

print(student.clear())

