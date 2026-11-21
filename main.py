from itertools import product
import os
from datetime import datetime, date

frame_width = 75

# Product data set storing table
product_data = []

def enter_product_date(inputed_date):
    # Prompt the user to enter a date in the format YYYY-MM-DD
    while True:
        date_string = input(inputed_date).strip()
        if date_string == "":
            # Return today's date if the input is empty
            return date.today().isoformat()  
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def add_inventory():
    def number_of_products():
        while True:
            try:
                num_products = int(input("Enter the number of products to add: "))
                if num_products <= 0:
                    print("Please enter a positive integer.")
                else:
                    return num_products
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def get_product_price():
        while True:
            try:
                price = float(input("Enter the product price: "))
                if price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                else:
                    return price
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_product_quantity(i):
        while True:
            try:
                quantity = int(input(f"Enter the quantity of product {i}: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please enter a valid quantity.")
                else:
                    return quantity
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    print("Add Inventory")
    num_products = number_of_products()           
    #Extra unnecessary code removed to avoid redundancy. The price is now collected for each product individually.
    #price = get_product_price()

    # Add the product to the inventory
    product_added = []

    for i in range(1, num_products + 1):
        product_name = input(f"Enter the name of product {i}: ")
        product_quantity = get_product_quantity(i)
        product_date = enter_product_date(f"Enter the date for product {i} (YYYY-MM-DD) or leave blank for today: ")
        # Use the same price for all products added in this batch
        product_price = get_product_price()
        
        #product_added.append([product_name, product_date, product_quantity, product_price])
        #product_added.append(product)
        
        product = {
            "Name": product_name,
            "Date": product_date,
            "Quantity": product_quantity,
            "Price": product_price,
        }
        product_data.append(product)
        product_added.append(product)

    print("=" * frame_width)
    print(f'{"#":<15}{"Add Inventory":^{frame_width - 30}}{"#":>15}')
    print("=" * frame_width)
    #print("\n" + "=" * frame_width)
    print(f"{"S.I":<6}{"Product Name":<20}{"Date":<15}{"Quantity":<10}{"Price":<10}{"Total":<12}")
    print("=" * frame_width)

    gross_price = 0
    for index, product in enumerate(product_added, start=1):
        total_price = float(product["Quantity"]) * float(product["Price"])
        gross_price += total_price
        print(f"{index:<6}{product['Name']:<20}{product['Date']:<15}{product['Quantity']:<10}{product['Price']:<10}{total_price:<12}")

    print("=" * frame_width)
    print(f"{"Gross Price#":<6}{"":<20}{"":<15}{"":<10}{"":<10}{gross_price:<2}")
    print("=" * frame_width)

    input("\nPress Enter to return to the main menu...")

def view_inventory():
    if not product_data:
        print("No products in inventory.")
        input("Press Enter to return to the main menu...")
        return

    print("=" * frame_width)
    print(f'{"#":<15}{"View Inventory":^{frame_width - 30}}{"#":>15}')
    print("=" * frame_width)
    #print("\n" + "=" * frame_width)
    print(f"{"S.I":<6}{"Product Name":<20}{"Date":<15}{"Quantity":<10}{"Price":<10}{"Total":<12}")
    print("=" * frame_width)

    gross_price = 0

    # Sort by product name
    sorted_inventory = sorted(product_data, key=lambda product: product["Name"])  
    #for index, product in enumerate(product_data, start=1):
    for index, product in enumerate(sorted_inventory, start=1):
        total_price = float(product["Quantity"]) * float(product["Price"])
        gross_price += total_price
        print(f"{index:<6}{product['Name']:<20}{product['Date']:<15}{product['Quantity']:<10}{product['Price']:<10}{total_price:<12}")

    print("=" * frame_width)
    print(f"{"Gross Price#":<6}{"":<20}{"":<15}{"":<10}{"":<10}{gross_price:<2}")
    print("=" * frame_width)

    input("\nPress Enter to return to the main menu...")

def save_inventory():
    # Save the product data to a file
    if not product_data:
        print("No products to save.")
        return

    try:
        with open("inventory_data.txt", "w") as file:
            file.write("=" * frame_width + "\n")
            file.write(f'{"#":<15}{"Inventory Data":^{frame_width - 30}}{"#":>15}\n')
            file.write("=" * frame_width + "\n")

            file.write(f"{"S.I":<6}{"Product Name":<20}{"Date":<15}{"Quantity":<10}{"Price":<10}{"Total":<12}\n")
            file.write("=" * frame_width + "\n")

            gross_price = 0

            for index, product in enumerate(product_data, start=1):
                total_price = float(product["Quantity"]) * float(product["Price"])
                gross_price += total_price
                file.write(f"{index:<6}{product['Name']:<20}{product['Date']:<15}{product['Quantity']:<10}{product['Price']:<10}{total_price:<12}\n")

            file.write("=" * frame_width + "\n")
            file.write(f"{"Gross Price#":<6}{"":<20}{"":<15}{"":<10}{"":<10}{gross_price:<2}\n")
            file.write("=" * frame_width + "\n")

        print("Inventory data saved to 'inventory_data.txt'.")

    except Exception as error_occured:
        print(f"An error occurred while saving inventory data: {error_occured}")

#def delete_inventory():

#def sale_inventory():

#def sale_history():



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
        print(f'{"#":<15}{"Inventory Management System":^{frame_width - 30}}{"#":>15}')
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
            while True:
                save_choice = input("Do you want to save the inventory data before exiting? (y/n): ").strip().lower()
                if save_choice == 'y':
                    save_inventory()
                    print("Inventory data saved successfully.")
                    break
                elif save_choice == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again by entring a number from 1-6.")
            input("Press Enter to proceed...")

main()