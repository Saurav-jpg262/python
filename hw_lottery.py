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

winning_numbers = {10,25,32,41,43,45,50}

# Check common numbers using intersection
found_numbers = user_numbers.intersection(winning_numbers)

count_correct_numbers = len(found_numbers)

# We can do a if/elif structure
#if count_correct_numbers == 3:
#    print("You won $4!")

prizes = {
    3: 4,
    4: 15,
    5: 200,
    6: 30000,
    7: 5000000
}

if count_correct_numbers in prizes:
    print(f"You won ${prizes[count_correct_numbers]}")
else:
    print("Sorry, you didn't win this time...")