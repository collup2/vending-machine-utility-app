items = {
    "D1": {"name": "Cola", "price": 3.00, "stock": 5},
    "D2": {"name": "Water", "price": 2.00, "stock": 5},
    "D3": {"name": "Coffee", "price": 5.00, "stock": 5},
    "S1": {"name": "Chocolate", "price": 4.00, "stock": 5},
    "S2": {"name": "Crisps", "price": 3.00, "stock": 5},
    "S3": {"name": "Biscuits", "price": 3.50, "stock": 5}
}

# This variable controls whether the vending machine keeps running
machine_running = True

# Main program loop
while machine_running:

    # Display the vending machine menu
    print("\n====== VENDING MACHINE MENU ======\n")

    print("DRINKS:")
    print("D1 - Cola (AED 3.00)")
    print("D2 - Water (AED 2.00)")
    print("D3 - Coffee (AED 5.00)\n")

    print("SNACKS:")
    print("S1 - Chocolate (AED 4.00)")
    print("S2 - Crisps (AED 3.00)")
    print("S3 - Biscuits (AED 3.50)\n")

    # Ask the user to select an item by entering its code
    choice = input("Enter the item code (e.g. D1, S2): ").upper()

    # Check if the entered code exists in the items dictionary
    if choice not in items:
        print("Invalid item code. Please try again.")
        continue

    # Check if the selected item is in stock
    if items[choice]["stock"] <= 0:
        print("Sorry, this item is out of stock.")
        continue

    # Store the selected item's price and name
    item_price = items[choice]["price"]
    item_name = items[choice]["name"]

    print(f"\nYou selected: {item_name}")
    print(f"Price: AED {item_price:.2f}")

    # Ask the user to insert money
    money_inserted = float(input("Insert money (AED): "))

    # Check if the user inserted enough money
    if money_inserted < item_price:
        print("Insufficient money. Transaction cancelled.")
        continue

    # Calculate change
    change = money_inserted - item_price

    # Reduce the stock of the selected item
    items[choice]["stock"] -= 1

    # Dispense item message
    print(f"\nDispensing {item_name}...")
    print("Enjoy your item!")

    # Display change if any
    print(f"Your change is AED {change:.2f}")

    # Simple intelligent suggestion system
    # If the user buys coffee, suggest biscuits
    if choice == "D3" and items["S3"]["stock"] > 0:
        print("\nSuggestion: Coffee goes well with Biscuits!")
        add_on = input("Would you like to buy Biscuits for AED 3.50? (yes/no): ").lower()

        if add_on == "yes":
            if change >= items["S3"]["price"]:
                items["S3"]["stock"] -= 1
                change -= items["S3"]["price"]
                print("Biscuits dispensed!")
                print(f"Remaining change: AED {change:.2f}")
            else:
                print("Not enough remaining balance for Biscuits.")

    # Ask if the user wants to buy another item
    again = input("\nWould you like to buy another item? (yes/no): ").lower()

    if again != "yes":
        machine_running = False

# End of vending machine program
print("\nThank you for using the Vending Machine!")
