marks = []

while True:
    user_mark = input("Enter a mark (press enter to stop):\n")
    if user_mark == "":
        break
    try:
        marks.append(float(user_mark))
    except ValueError:
        print("Invalid input. Please enter a number or press Enter to stop")

#total = 0
#for mark in marks:
#    total += mark

#average = total / len(marks)

average =  sum(marks) / len(marks)
print(f"The average is: {round(average, 2)}")
   