# The elif Statement
# elif stands for else if. It is used to check multiple conditions.
# if any condition is true then it ignores other conditions even if its true.

score = 75
 
if score >= 90:
    print("Grade A")
elif score >= 60:
    print("Grade B")
elif score>=40:                       #this condition is also true but the previous condition is also true so it ignores these conditions
     print("Grade C")
else:
    print("Grade C")



