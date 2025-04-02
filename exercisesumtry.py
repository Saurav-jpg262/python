total = 0

while True:
    try:
        number = int(input("Enter the number:  "))
        if number == 0:
            break
        else:
            total += number
    except ValueError:
        print("Invalid, please enter only numbers")

print(f"the total is: {total}")