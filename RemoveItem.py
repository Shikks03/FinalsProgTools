import AccessDatabase

def removeItem():
    while True: # will loop until valid input
        item = input("Enter the item name to remove: ")
        if not item.isalpha():
            print("Invalid name. Please enter alphabetic characters only.")
        else:
            break
    if not AccessDatabase.checkItemName(item): #check if item exists, if not then it just ends here
        exit()
    if item in AccessDatabase.sample:
        AccessDatabase.sample.remove(item)
        print(f"Item '{item}' removed from the database.")
    #need to add a part where it removes everything related to that name
