import random
min_number = 0
max_number = 10
correct_number = random.randint(min_number, max_number)

while True:
    try:
        user_number = int(input(f"Guess a number between {min_number} and {max_number}\n"))
        if user_number == correct_number:
            print("You won")
            break
        elif user_number > correct_number:
            print("This is too high")
        else:
            print("This is too low")
    except ValueError:
        print("Invalid. Only numbers are allowed.")