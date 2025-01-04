age = 30
message = "Eligible" if age >= 40 else "not eligible"
print(message)

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

print(10 > 3)
required_age = 18
age = int(input("Enter your age: "))
if age >= required_age:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

messages = "Eligible to vote" if age >= required_age < 60 else "Not eligible"
print(messages)

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")
