import AccessDatabase
import AddItem

def UpdateItem(old_item, new_item):
    if old_item in AccessDatabase.sample: #looking for the item then updating it
        index = AccessDatabase.sample.index(old_item)
        AccessDatabase.sample[index] = new_item
        print(f"Item '{old_item}' updated to '{new_item}' in the database.")
    else:
        print(f"Item '{old_item}' not found in the database.")


def whatToUpdate():
    while True: # will loop until valid input
        item = input("Enter the item name to update: ")
        if not item.isalpha():
            print("Invalid name. Please enter alphabetic characters only.")
        else:
            break
        if not AccessDatabase.checkItemName(item): 
            exit() #if hindi nakita ung item sa database then the function ends

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
            old_name = item
            new_name = input("Enter the new item name: ")
            UpdateItem(old_name, new_name)
            break
        elif choice == '2':
            print("\nUpdating item quantity")
            old_quantity = AccessDatabase.sample[2]  # this is if the quantity is stored at index 2
            new_quantity = input("Enter the new item quantity: ")
            UpdateItem(old_quantity, new_quantity)
            break
        elif choice == '3':
            print("\nUpdating item category")
            old_category = AccessDatabase.sample[3]  # this is if the category is stored at index 3
            new_category = AddItem.itemCategory()
            UpdateItem(old_category, new_category)
            break

whatToUpdate()
