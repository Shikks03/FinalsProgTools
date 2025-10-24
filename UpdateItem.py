import AccessDatabase
import AddItem

def UpdateItem(item, type, old, new): #no fixed data type
    oldItem = item[type]
    if oldItem == old:
        item[type] = new
        print(f"Item {type} '{old}' updated to '{new}' in the database.")
    else:
        print("Error matching items.")


def whatToUpdate():
    while True: # will loop until valid input\
        choice = input("Enter the ID to update: ")
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        choice = int(choice)
        if choice < 1 or choice > len(AccessDatabase.inventory):
            print("Invalid ID. Please enter a valid one.")
            continue
        break

    item = AccessDatabase.inventory[choice-1]

    while True: #while loop until valid choice input
        print(f"What would you like to update for the item '{item}'?")
        print("1. Item Name")
        print("2. Item Quantity")
        print("3. Item Category")
        choice = input("Enter your choice (1-3): ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
            print("Invalid option. Please enter a number between 1 to 3.\n")
        elif choice == '1':
            print("\nUpdating item name")
            old = item["name"]
            new = AddItem.itemName()
            UpdateItem(item, "name", old, new)
            break
        elif choice == '2':
            print("\nUpdating item quantity")
            old = item["quantity"]
            new = AddItem.itemQuantity()
            UpdateItem(item, "quantity", old, new)
            break
        elif choice == '3':
            print("\nUpdating item category")
            old = item["category"]
            new = AddItem.itemCategory()
            UpdateItem(item, "category", old, new)
            break
    AccessDatabase.saveDatabase()
