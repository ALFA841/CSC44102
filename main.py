from itertools import product
import os
from datetime import datetime, date
import csv

frame_width = 75

# Product dataset storing table.
product_data = []
# This list is to store sale history dataset.
sale_history_data = []

def preload_datasets():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder_path, "product_data.csv")
    # Preload product dataset from a CSV file
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as product_file:
            reader = csv.DictReader(product_file, skipinitialspace=True)
            for row in reader:
                product = {
                        "Name": row["product_name"],
                        "Date": row["product_date"],
                        "Quantity": float(row["product_quantity"]),
                        "Price": float(row["product_price"])
                        }
                product_data.append(product)
    except FileNotFoundError:
        print("Product data file not found. Starting with an empty product dataset.")
        pass

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

# This helper function is to get the products that are in stock (quantity > 0) and sort them alphabetically by product name.
def ready_products():
    product_in_stock = []

    for product in product_data:
        #in stock product are only shown in the inventory for this condition.
        if product["Quantity"] > 0:
            product_in_stock.append(product)

    #Sorting operation in alphabetical order of the product names to make it easier for the user to find a specific product in stock.
    product_in_stock.sort(key=lambda product: product["Name"])
    return product_in_stock

def view_inventory():
    products_ready_for_sale = ready_products()
    if not products_ready_for_sale:
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
    sorted_inventory = sorted(products_ready_for_sale, key=lambda product: product["Name"])
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
    products_ready_for_sale = ready_products()
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

            for index, product in enumerate(products_ready_for_sale, start=1):
                total_price = float(product["Quantity"]) * float(product["Price"])
                gross_price += total_price
                file.write(f"{index:<6}{product['Name']:<20}{product['Date']:<15}{product['Quantity']:<10}{product['Price']:<10}{total_price:<12}\n")

            file.write("=" * frame_width + "\n")
            file.write(f"{"Gross Price#":<6}{"":<20}{"":<15}{"":<10}{"":<10}{gross_price:<2}\n")
            file.write("=" * frame_width + "\n")

        print("Inventory data saved to 'inventory_data.txt'.")

    except Exception as error_occured:
        print(f"An error occurred while saving inventory data: {error_occured}")

def delete_inventory():
    products_ready_for_sale = ready_products()
    if not products_ready_for_sale:
        print("No products in inventory to delete.")
        input("Press Enter to return to the main menu...")
        return

    print("=" * frame_width)
    print(f'{"#":<15}{"Delete Inventory":^{frame_width - 30}}{"#":>15}')
    print("=" * frame_width)
    #print("\n" + "=" * frame_width)
    print(f"{"S.I":<6}{"Product Name":<20}{"Date":<15}{"Quantity":<10}{"Price":<10}{"Total":<12}")
    print("=" * frame_width)
    #Options to delete a product completely or delete a specific quantity of a product
    print("1. Delete a product completely")
    print("2. Delete a specific quantity of a product")
    print("3. Return back to the main menu")
    print("=" * frame_width)
    user_choice = input("Enter your choice (1-3): ")

    if user_choice == '3':
        print("Returning to the main menu...")
        return

    elif user_choice not in ['1', '2']:
        print("Invalid choice. Returning to the main menu...")
        return

    #Display the inventory for the user to know the products before deletion 
    sorted_inventory = sorted(products_ready_for_sale, key=lambda product: product["Name"])

    print("=" * frame_width)
    print(f"{"S.I":<6}{"Product Name":<20}{"Date":<15}{"Quantity":<10}{"Price":<10}{"Total":<12}")
    print("=" * frame_width)

    for index, product in enumerate(sorted_inventory, start=1):
        total_price = float(product["Quantity"]) * float(product["Price"])
        print(f"{index:<6}{product['Name']:<20}{product['Date']:<15}{product['Quantity']:<10}{product['Price']:<10}{total_price:<12}")

    print("=" * frame_width)

    try:
        delete_index = int(input("Enter the S.I of the product to delete (or 0 to cancel): "))
        if delete_index == 0:
            print("Deletion cancelled.")
            return
        elif 1 <= delete_index <= len(products_ready_for_sale):
            if user_choice == '1':
                #Here the product is deleted completely from the inventory
                deleted_product = products_ready_for_sale.pop(delete_index - 1)
                print(f"Deleted product: {deleted_product['Name']}")
            elif user_choice == '2':
                """
                Here the user is prompted to enter the quantity to delete from the selected product. 
                If the quantity to delete is greater than or equal to the current quantity, the product is deleted completely. 
                Otherwise, the specified quantity is subtracted from the product's quantity.
                """
                quantity_to_delete = int(input("Enter the quantity to delete: "))
                if quantity_to_delete <= 0:
                    print("Quantity must be a positive integer. Deletion cancelled.")
                    return
                elif quantity_to_delete >= products_ready_for_sale[delete_index - 1]["Quantity"]:
                    deleted_product = products_ready_for_sale.pop(delete_index - 1)
                    print(f"Deleted product: {deleted_product['Name']}")
                else:
                    products_ready_for_sale[delete_index - 1]["Quantity"] -= quantity_to_delete
                    print(f"Deleted {quantity_to_delete} from product: {products_ready_for_sale[delete_index - 1]['Name']}")
        else:
            print("Invalid S.I. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def sale_inventory():
    products_ready_for_sale = ready_products()

    if not products_ready_for_sale:
        print("No products in stock for sale.")
        input("Press Enter to return to the main menu...")
        return

    print("=" * frame_width)
    print(f'{"#":<15}{"Sale Inventory":^{frame_width - 30}}{"#":>15}')
    print("=" * frame_width)
    print(f"{"S.I":<6}{"Product Name":<20}{"Quantity":<10}{"Price":<10}{"Total":<12}")
    print("=" * frame_width)

    for index, product in enumerate(products_ready_for_sale, start=1):
        total_price = float(product["Quantity"]) * float(product["Price"])
        print(f"{index:<6}{product['Name']:<20}{product['Quantity']:<10}{product['Price']:<10}{total_price:<12.2f}")
    print("=" * frame_width)

    try:
        sale_index = int(input("Enter the S.I of the product to sell (or 0 to cancel): "))

        if sale_index == 0:
            print("Sale cancelled.")
            return
        elif 1 <= sale_index <= len(products_ready_for_sale):
            selected_product = products_ready_for_sale[sale_index - 1]
            quantity_to_sell = int(input(f"Enter the quantity to sell for {selected_product['Name']}: "))
            if quantity_to_sell <= 0:
                print("Quantity must be a positive integer. Sale cancelled.")
                return
            elif quantity_to_sell > selected_product["Quantity"]:
                print(f"Not enough stock. Available quantity: {selected_product['Quantity']}. Sale cancelled.")
                return
            else:
                # Update the product quantity in the main product_data list
                for product in product_data:
                    if product["Name"] == selected_product["Name"] and product["Date"] == selected_product["Date"]:
                        product["Quantity"] -= quantity_to_sell
                        break

                # Record the sale in the sale_history_data list
                sale_record = {
                    "Name": selected_product["Name"],
                    "Date": date.today().isoformat(),
                    "Quantity Sold": quantity_to_sell,
                    "Price": selected_product["Price"],
                    "Total Sale": quantity_to_sell * selected_product["Price"]
                }
                sale_history_data.append(sale_record)

                print(f"Sold {quantity_to_sell} of {selected_product['Name']}.")
        else:
            print("Invalid S.I. Please enter a valid number.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def product_sale_performance_graph():
    print("Function 'Product Sale Performance Graph' is not yet implemented.")
    print("Press Enter to return to the main menu...")
    input()


def main():
    # Define the main menu options
    main_menu = [
        "1. View Inventory",
        "2. Add Inventory",
        "3. Delete Inventory",
        "4. Sale Inventory",
        "5. Product Sale Performance Graph",
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
            os.system('cls' if os.name == 'nt' else 'clear')
            add_inventory()
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            delete_inventory()
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            sale_inventory()
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            product_sale_performance_graph()
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

preload_datasets()
main()