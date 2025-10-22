sample = ["shikkari", "33", "Food"]

#maybe put a temporary variable that is lowercased for checking purposes
#then append the original input to the database

def checkItemName(name):
    if name in sample:
        print(f"\nItem '{name}' found in the database.")
        return True
    else:
        print(f"\nItem '{name}' not found in the database.")
        return False
    

#i think it would be best if mag dictionary na lang ung database to store all the details of the item
#like item name, quantity, category, etc.
testingDictionary = {
    "0001": {"name": "Shikkari", "quantity": 33, "category": "technology"},
    "0002": {"name": "Bea", "quantity": 20, "category": "books"}
} #   itemID       name           quantity        category