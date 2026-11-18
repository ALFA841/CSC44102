import os

frame_width = 50

def main():
    # Define the main menu options
    main_menu = [
        "1. View Inventory",
        "2. Add Inventory",
        "3. Delete Inventory",
        "4. Sale Inventory",
        "5. Sale History",
        "6. Exit"
    ]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print the main menu with a frame
        print("=" * frame_width)
        print(f'{"#":<12}{"Inventory Management System":^{frame_width - 30}}{"#":>11}')
        print("=" * frame_width)
        #print()

        for option in main_menu:
            print(f"{"#":<15}{option:^{frame_width - 30}}{"#":>15}")
        
        print("=" * frame_width)

        choice = input("Enter your choice (1-6): ")

        # Here the functions view_inventory, add_inventory, delete_inventory, sale_inventory, and sale_history
        # should be defined elsewhere in the code and is not yet made.
        if choice == '1':
            view_inventory()   
        elif choice == '2':
            add_inventory()
        elif choice == '3':
            delete_inventory()
        elif choice == '4': 
            sale_inventory()
        elif choice == '5':
            sale_history()
        elif choice == '6':
            print("Exiting the program...")
            break

main()