import AccessDatabase

def displayItems():
    if AccessDatabase.sample:
        print("Items in the database:")
        for item in AccessDatabase.sample:
            print(f"- {item}") #or make it formatted better
    else:
        print("The database is empty.")