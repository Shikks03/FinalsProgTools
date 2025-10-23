import AccessDatabase

def removeItem():
    while True:
        choice = input("Enter the ID to remove: ")
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        choice = int(choice)
        if choice < 1 or choice > len(AccessDatabase.inventory):
            print("Invalid ID. Please enter a valid one.")
            continue
        break

    item = AccessDatabase.inventory.pop(choice - 1)
    print(f"Item '{item['name']}' removed from the database.")
    AccessDatabase.saveDatabase()
