import AccessDatabase

def displayItems():
    AccessDatabase.loadDatabase()
    if AccessDatabase.inventory:
        print("Items in the database:")
        print("id   name           quantity   category")
        for i, item in enumerate(AccessDatabase.inventory):
            print(f"{(i+1):<4} {item["name"]:<15} {item["quantity"]:<10} {item["category"]}")
    else:
        print("The database is empty.")