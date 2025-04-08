user_numbers = set()
while True:
    if len(user_numbers) >= 7:
        break
    try:
        user_input = int(input(f"Enter a number {len(user_numbers)+1}/7 : \n"))
        if user_input in user_numbers:
            print("You already entered that number")
        else:
            user_numbers.add(user_input)
    except ValueError:
        print("Please enter only numbers")
print("Your lottery numbers are:")
for number in user_numbers:
    print(number)