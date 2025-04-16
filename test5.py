numbers = []

while True:
    user = input("Enter the number or press enter button to stop: ")
    if user == "":
        break
    else:
        numbers.append(int(user))

choose = input("Do you want to print the max (press 1) or minimum number (press 2)? ")

if choose == "1":
    print("The max is:", max(numbers))
elif choose == "2":
    print("The minimum is:", min(numbers))
else:
    print("Invalid choose.")