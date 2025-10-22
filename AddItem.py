import AccessDatabase

def addItem(item): # function for adding an item to the database
    AccessDatabase.sample.append(item)
    print(f"Item '{item}' added to the database.")

def checkDuplicate(item): #function for checking duplicates
    item.islower() #make sure to lowercase items when checking
    if item in AccessDatabase.sample:
        print(f"Item '{item}' already exists in the database.")
        return True
    return False

def itemName(): #inputting name w/ error handling (letters only)
    while True:
        name = input("Enter item name: ")
        if not name.isalpha():
            print("Invalid name. Please enter alphabetic characters only.")
        else:
            break
    return name

def itemQuantity(): #inputting quantity w/ error handling (numbers only)
    while True:
        quantity = input("Enter item quantity: ") #error check
        if not quantity.isdigit():
            print("Invalid quantity. Please enter numeric characters only.")
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
        if not categoryOption.isdigit() and categoryOption <= 0 and categoryOption > 5: #1-5 categories
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
    print("\nAdding a new item")

    name = itemName()

    quantity = itemQuantity()

    category = itemCategory()
    
    dictionaryItem = {
        "name": name,
        "quantity": quantity,
        "category": category
    } #if you want to make it a dictionary

    stringItem = f"{name} - {quantity} - {category}" #if you want to make it a string
    arrayItem = [name, quantity, category] #if you want to make it an array

    addItem(name) #change to dictionaryItem or arrayItem or stringItem
    addItem(quantity)
    addItem(category)
