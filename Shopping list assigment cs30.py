# cs30 FP1-F02 "Shopping List) - Carter Flanagan

#defining menu
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. Modify item")
    print("3. Delete item")
    print("4. View shopping list")
    print("5. Calculate total cost")
    print("6. Exit")
#defining item addition
def add_item(shopping_list):
    item = input("Enter the item name: ")
    try:
        cost = float(input("Enter the cost of the item: "))
        shopping_list[item] = cost
        print(f"Added {item} with a cost of ${cost:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid cost.")
#defining item modification
def modify_item(shopping_list):
    item = input("Enter the item you want to modify: ")
    if item in shopping_list:
        try:
            new_cost = float(input(f"Enter the new cost for {item}: "))
            shopping_list[item] = new_cost
            print(f"Modified {item} to a new cost of ${new_cost:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid cost.")
    else:
        print(f"{item} not found in the shopping list.")
#defining item removal
def delete_item(shopping_list):
    item = input("Enter the item you want to delete: ")
    if item in shopping_list:
        del shopping_list[item]
        print(f"Deleted {item} from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")
#defining vieing the list
def view_shopping_list(shopping_list):
    if shopping_list:
        print("\nShopping List:")
        for item, cost in shopping_list.items():
            print(f"{item}: ${cost:.2f}")
    else:
        print("The shopping list is empty.")
#tells the total cost of items
def calculate_total_cost(shopping_list):
    total_cost = sum(shopping_list.values())
    print(f"\nTotal cost of shopping list: ${total_cost:.2f}")
#main menu
def main():
    shopping_list = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            modify_item(shopping_list)
        elif choice == '3':
            delete_item(shopping_list)
        elif choice == '4':
            view_shopping_list(shopping_list)
        elif choice == '5':
            calculate_total_cost(shopping_list)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 6.")
#runs the program
if __name__ == "__main__":
    main()
