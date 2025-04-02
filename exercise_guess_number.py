import random

my_number = random.randint(0,10)
while True:
    guess_number = int(input("Enter the number:  "))
    if guess_number <  my_number:
        print("guess number is small , enter big:  ")

    elif guess_number > my_number:
        print("your guess number is big , enter the small")
    else:
        print("you are correct")
        break
