import AccessDatabase

def searchItem():
    totalHits = 0
    name = input("Enter the item name to search: ").lower()

    print("id   name           quantity   category")
    for i, item in enumerate(AccessDatabase.inventory):
        if name in item["name"].lower():  # check if search term is contained in item name
            print(f"{(i+1):<4} {item['name']:<15} {item['quantity']:<10} {item['category']}")
            totalHits += 1

    if totalHits == 0:
        print("No results found.")
    else:
        print(f"{totalHits} result(s) found.")


#wla pang error handling
#make sure to islowercase when checking