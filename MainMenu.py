import AddItem
import RemoveItem
import ViewItem
import SearchItem
# import UpdateItem



while True:
    print("\nWelcome to the Inventory System!")
    print("1. Add Item") #Create
    print("2. Remove Item") #Delete
    print("3. View Items") #Read
    print("4. Search Item") #Search
    print("5. Update Item") #Update
    print("6. Exit")
    choice = input("Please select an option (1-6): ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > 6:
        print("Invalid option. Please enter a number between 1 to 6.")
    elif choice == '1':
        AddItem.getItemDetails()
    elif choice == '2':
        #call the remove item module
        RemoveItem.removeItem()
    elif choice == '3':
        print("Viewing items...")
        ViewItem.displayItems()
    elif choice == '4':
        #call the search item module
        SearchItem.searchItem()
    elif choice == '5':
        #call the update item module
        print("Updating item...")
    elif choice == '6':
        print("Exiting the system...")
        exit()