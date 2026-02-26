name = input()           #here we are taking i/p without a prompt and By default, all input taken using input() is of string data type
print(name)
print(type(name))

gender = input("Please enter your gender:")               #input with a prompt,prompt is optional not compulsory
print(gender)

age = input("Enter your age: ")                           #whatever we want to print can also be written using multipe
print(age)
print(type(age))                                          #if we want to add age+5 we cant because by default age is a string data type
                                                      
price =int(input("Enter the price of bat: "))             #so to perform mathematical calculations we should write in this way 
print("After the discount the actual price is",price-20)
print(type(price))

quantity=float(input("Enter the quantity:"))
totalprice = price*quantity - quantity*20
print("The total price is ",totalprice)
