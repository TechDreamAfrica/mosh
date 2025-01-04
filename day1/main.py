print("Hello World")
print(20)
print(10 + 2)
print(3 * 9)

#Variables
name = "Godfred"
print(name)

first_name = "Andy"
last_name = "Kofi Andoh"
full_name = first_name + " " + last_name
print(full_name)

#You can join two variables with comma
f_name = "Ebenezer"
l_name = "Tetteh"
print(f_name, l_name)

#You can concatenate strings with numbers
name = "Divina"
age = 40
print("Name: ", name, "Age: ", age)

#Data Types
#Booleans
is_student = True
print(type(is_student))
print(is_student)

#Strings
brand = "hp"
print(brand)
print(brand.upper())
print(brand.capitalize())
print(brand.startswith("p"))
print(brand.find("h"))
print(brand.index("p"))

#Float
weight = 35.78
print(weight)

cement = "Dangote"
weight = 50
price = 120
details = "Name  | Weight  | price"
print(details.upper())
print(cement, weight, price)

#Type Casting
#Concatenation
product = "Itel A20"
price = 1500.34
state = "New"
quantity = 4

print("Name: " + product + " " + "Price:" + " " + str(price) + " " + "State:" + " " + state + " " + "Quantity:" + " " + str(quantity))
print("Name:", product, "Price:", price, "State", state, "Quantity:", quantity)
print(f"Name: {product} Price: {price} State:{state} Quantity: {quantity}")