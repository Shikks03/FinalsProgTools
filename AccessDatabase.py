import os

inventory = []
maxid = 1

def checkItemName(name):
    for item in inventory:
        if name.lower() == item["name"].lower():
            print(f"\nItem '{name}' found in the database.")  # debug
            return True
    print(f"\nItem '{name}' not found in the database.")  # debug
    return False

def loadDatabase():
    global inventory, maxid  # tell Python to use the global variables
    if os.path.exists("database.txt"):
        print("Loading database...")
    else:
        print("No database file found, creating new database file...")
        open("database.txt", "w").close()

    inventory = []
    with open("database.txt", "r") as file:
        for line in file:
            if line.strip():
                name, quantity, category = line.strip().split(", ")
                inventory.append({
                    "name": name,
                    "quantity": int(quantity),
                    "category": category
                })
                maxid += 1  # safely updates global variable

def saveDatabase():
    with open("database.txt", "w") as file:
        for item in inventory:
            file.write(f"{item['name']}, {item['quantity']}, {item['category']}\n")
    print("Database saved successfully!")
