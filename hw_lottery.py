numbers = set()

while len(numbers) < 7:
    number = int(input("Enter a number:\n "))
    

    if number in numbers:
        print("You already entered this number. Try a different one.")
    else:
        numbers.add(number)

print("Your numbers are:", numbers)

winning_numbers = {10, 25, 32, 41, 43, 45, 50}


correct = numbers & winning_numbers  
count = len(correct)


if count == 3:
    print("You win $4")
elif count == 4:
    print("You win $15")
elif count == 5:
    print("You win $200")
elif count == 6:
    print("You win $30000")
elif count == 7:
    print("You win $5,000,000")
else:
    print("Sorry, no prize.")

print("Correct numbers:"correct)