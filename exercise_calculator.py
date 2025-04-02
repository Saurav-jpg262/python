number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter an operator: ")
result = None

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 == 0:
        print("Error: division by 0 is not allowed")
    else:
        result = number1 / number2
else:
    print("Invalid operator")

if (result is not None):
    print(f"Total is {result}")