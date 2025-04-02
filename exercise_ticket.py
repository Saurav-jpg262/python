age = int(input("Enter your age: "))

if (age >= 18):
    price = 10
elif (age >= 4 and age <18):
    price = 8
else:
    price = 5

print(f"Your ticket price is ${price}")