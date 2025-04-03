attempts = 0
max_attempts = 5
answer = "Tokyo"

while True:
    capital_city = input("What is the capital city of Japan?:  ")
    attempts += 1

    if capital_city == answer:
        print("Your answer is correct.")
        break

    if attempts == max_attempts:
        print("You are out of attempts. The correct answer is Tokyo.")
        break

    print(f"Incorrect. Attempts: {attempts}/{max_attempts}")