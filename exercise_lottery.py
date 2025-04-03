user_numbers = set()


while True:
    if len(user_numbers) == 7:
        break
    try:
        number = int(input(f"Enter a number {len(user_numbers)+1}/7:  "))

        if number in user_numbers:
            print("Number is already their, Please another number")
        else:
            user_numbers.add(number)
    except ValueError:
        print("Please enter value number")
for number in user_numbers:
    print(number)
