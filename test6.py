def atm():
    balance = 1000
    correct_pin = 5555
    pin_attempts = 0
    max_attempts = 3
    
    while pin_attempts < max_attempts:
        pin = int(input("Enter your PIN: "))
        
        if pin == correct_pin:
            print("You are welcome.")
            break
        else:
            pin_attempts += 1
            if pin_attempts < max_attempts:
                print(f"Incorrect PIN. You have {max_attempts - pin_attempts} attempts left.")
            else:
                print("You have reached you maximum attempt. Your card is blocked")
                return 

    while True:
        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = int(input("Enter your choice (1/2/3/4): "))
    if choice == 1:
            deposit_amount = float(input("Enter amount to deposit: "))
            balance += deposit_amount
            print(f"Deposited ${deposit_amount}. Current Balance: ${balance:.2f}")    

    elif choice == 2:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
                print(" Error: Insufficient funds.")
        else:
            balance -= withdraw_amount
            print(f"Withdrew ${withdraw_amount}. Current Balance: ${balance:.2f}")

    elif choice == 3:
        print(f"### Current Balance: ${balance:.2f}")

    elif choice == 4:
        print("Exiting. Thank you!")
        
   
    else:
        print("Invalid option. Please choose again.")
atm()