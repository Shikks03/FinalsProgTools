import AccessDatabase

def searchItem(item):
    if item in AccessDatabase.sample:
        print(f"Item '{item}' found in the database.")
    else:
        print(f"Item '{item}' not found in the database.")

searchKey = input("Enter the item name to search: ")
searchItem(searchKey)
#wla pang error handling
#make sure to islowercase when checking