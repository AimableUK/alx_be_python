def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Item name: ")
            shopping_list.append(item)

        elif choice == '2':
            item = input("Enter Item name to delete: ")
            for i in range(len(shopping_list)):
                if item == shopping_list[i]:
                    shopping_list.remove(item)
                    print("Item Deleted Successfully!!")
            else:
                print("Item Not Found.")


        elif choice == '3':
            print(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
