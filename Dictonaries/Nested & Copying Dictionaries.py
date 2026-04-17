student = {"name":"mohan","roll no" :25,"city":"delhi"}

# Copying Dictionaries

# copy()
# Creates a shallow copy of the dictionary.

new_student = student.copy()
student["name"]="manju"
print(new_student)



# Nested Dictionaries

# Dictionaries can contain other dictionaries.
student = {
    "fname":"sam",
    "lname":"bill",
    "age": 20,
     "marks": {
        "maths":96,
        "physics": 81
    }
}

# Accessing nested values:
print(student["fname"])
print(student["fname"]+" "+ student["lname"])

friends={
    "friend1":{
    "name:":"shru",
    "hobby":"writing,reading,eating",
    "college":"KU"
    },
    "friend2":{
    "name:":"ansh",
    "hobby":"sports,travel,gaming",
    "college":"RYMEC"

    }}
print(friends["friend1"])
print(friends["friend2"]["hobby"])
