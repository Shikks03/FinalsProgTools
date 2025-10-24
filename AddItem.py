import AccessDatabase

def addItem(item): # function for adding an item to the database
    AccessDatabase.inventory.append(item)
    print(f"name: {item["name"]} quantity: {item["quantity"]} category: {item["category"]} ") #for debug 
    print(f"'{item["name"]}' has been added to the database.")
    AccessDatabase.saveDatabase()

def checkDuplicate(name):  # check if item name already exists
    for item in AccessDatabase.inventory:
        if item["name"].lower() == name.lower():
            return True
    return False

def itemName(): #inputting name w/ error handling (letters only and spaces)
    while True:
        name = input("Enter item name: ")
        if not name.strip() or not all(c.isalpha() or c.isspace() for c in name):
            print("Invalid name. Please enter letters and spaces only.")
        elif checkDuplicate(name):
            print(f"Item '{name}' already exists.")
        else:
            break
    return name

def itemQuantity(): #inputting quantity w/ error handling (numbers only)
    while True:
        quantity = input("Enter item quantity: ") #error check
        if not quantity.isdigit():
            print("Invalid quantity. Please enter numeric characters only.")
        elif int(quantity) > 100:
            print("Quantity too big. Please enter a quantity 100 or lower.")
        else:
            break
    return quantity

def itemCategory(): #inputting category w/ error handling (numbers only for options)
    while True:
        print("Select item category:")
        print("1. Food")
        print("2. Drinks")
        print("3. Clothing")
        print("4. Technology")
        print("5. Books")
        categoryOption = input("Enter item category: ")
        if not categoryOption.isdigit() or (int(categoryOption) <= 0 or int(categoryOption) > 5): #1-5 categories
            print("Invalid category. Please enter numeric characters only.")
        else:
            break
    if categoryOption == '1':
        category = "Food"
    elif categoryOption == '2':
        category = "Drinks"
    elif categoryOption == '3':
        category = "Clothing"
    elif categoryOption == '4':
        category = "Technology"
    elif categoryOption == '5':
        category = "Books"
    return category
    

def getItemDetails(): # basically calls all the function to combine the details of the item
    AccessDatabase.loadDatabase()
    
    print("\nAdding a new item")

    name = itemName()

    quantity = itemQuantity()

    category = itemCategory()
    
    dictionaryItem = {
        "name": name,
        "quantity": quantity,
        "category": category
    } #if you want to make it a dictionary

    addItem(dictionaryItem) #change to dictionaryItem or arrayItem or stringItem

AccessDatabase.loadDatabase()