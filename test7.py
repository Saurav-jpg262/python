inventory = []

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    inventory.append({'name': name, 'quantity': quantity, 'price': price})
    print(f"Added item: {name} with quantity: {quantity} and price: ${price: }\n")

def view_inventory():
    if not inventory:
        print("Inventory is empty.\n")
    else:
        print("Current Inventory:")
        for item in inventory:
            print(f"- {item['name']}: Quantity = {item['quantity']}, Price = ${item['price']: }")
        print()

def calculate_total_value():
    total_value = sum(item['quantity'] * item['price'] for item in inventory)
    print(f" Total Inventory Value: ${total_value: }\n")

def inventory_menu():
    while True:
        print("Choose an option:")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Calculate Total Inventory Value")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            calculate_total_value()
        elif choice == '4':
            print("Exiting inventory system.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.\n")


inventory_menu()
