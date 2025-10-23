import os

inventory = []

#maybe put a temporary variable that is lowercased for checking purposes
#then append the original input to the database

#ano to
# def checkItemName(name):
#     if name in inventory:
#         print(f"\nItem '{name}' found in the database.")
#         return True
#     else:
#         print(f"\nItem '{name}' not found in the database.")
#         return False

def loadDatabase():
    if os.path.exists("database.txt"):
        # print("Loading database...")
    else:
        print("No database file found, creating new database file...")
        open("database.txt", "w").close() #create file if none found

    with open("database.txt", "r") as file:
            for line in file:
                name, quantity, category = line.strip().split(", ") #split using ,. and strip to remove extra spaces sa ends
                inventory.append({"name": name, "age": int(quantity), "category": category}) #add to variables

def saveDatabase():
    with open("database.txt", "w") as file:
        for item in inventory:
            file.write(f"{item['name']}, {item['quantity']}, {item['category']}\n")
    print("Database saved successfully!")

loadDatabase()
saveDatabase()

#i think it would be best if mag dictionary na lang ung database to store all the details of the item
#like item name, quantity, category, etc.
# item = {
#     "0001": {"name": "Shikkari", "quantity": 33, "category": "technology"},
#     "0002": {"name": "Bea", "quantity": 20, "category": "books"}
# } #   itemID       name           quantity        category