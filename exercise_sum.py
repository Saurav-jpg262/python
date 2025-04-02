variable_total = 0
data = 0
while True:
    data = int(input("Enter the number:  "))
    if data != 0:
        variable_total = variable_total + data
        
    else:
         print("The program end")
         break
    
print(f"The total is {variable_total}")

