# pylint: disable=wildcard-import
# pylint:disable=unused-wildcard-import
from crud import *
from archive import *
import os

# pylint: disable=missing-function-docstring
# pylint: disable=wildcard-import


def menu():
    print("\n--- INVENTORY SYSTEM (CSV) ---")
    print("1. Add product")
    print("2. Show products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save CSV (auto)")
    print("8. Load CSV")
    print("9. Exit")


# ======================
# NAME VALIDATION
# ======================
def get_valid_name():
    while True:
        name = input("Product name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        valid = True
        has_letter = False

        for char in name:
            if char.isalpha():
                has_letter = True
            elif char.isdigit() or char == " ":
                continue
            else:
                valid = False
                break

        if not valid:
            print("Only letters, numbers and spaces are allowed.")
            continue

        if not has_letter:
            print("Name cannot be only numbers.")
            continue

        return name


# ======================
# FLOAT VALIDATION (> 0)
# ======================
def get_valid_float(message):
    while True:
        value = input(message).strip()

        if not value:
            print("Value cannot be empty.")
            continue

        value = value.replace(",", ".")

        try:
            number = float(value)

            if number <= 0:
                print("Value must be greater than 0.")
                continue

            return number

        except ValueError:
            print("Invalid number. Use format like 10.5 or 10,5")


# ======================
# INTEGER VALIDATION (> 0)
# ======================
def get_valid_int(message):
    while True:
        value = input(message).strip()

        if not value:
            print("Value cannot be empty.")
            continue

        if not value.isdigit():
            print("Only whole numbers allowed.")
            continue

        number = int(value)

        if number <= 0:
            print("Value must be greater than 0.")
            continue

        return number


# ======================
# MAIN LOOP
# ======================
if __name__ == "__main__":
    while True:
        try:
            menu()
            option = input("Choose an option: ").strip()

            # ADD
            if option == "1":
                name = get_valid_name()
                price = get_valid_float("Price: ")
                quantity = get_valid_int("Quantity: ")

                create_product_csv({"name": name, "price": price, "quantity": quantity})
                print(f"\n✔ Product '{name}' added successfully.")

            # SHOW
            elif option == "2":
                products = read_products_csv()

                if not products:
                    print("Inventory is empty.")
                else:
                    print("\n--- INVENTORY ---")
                    print(f"{'#':<3} {'Name':<20} {'Price':<10} {'Quantity':<10}")
                    print("-" * 50)

                    for i, p in enumerate(products, 1):
                        print(
                            f"{i:<3} {p['name']:<20} ${p['price']:<9.2f} {p['quantity']:<10}"
                        )

            # SEARCH
            elif option == "3":
                name = get_valid_name()
                products = read_products_csv()

                result = search_product(products, name)

                if result:
                    print("\n--- PRODUCT FOUND ---")
                    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10}")
                    print("-" * 40)
                    print(
                        f"{result['name']:<20} ${result['price']:<9.2f} {result['quantity']:<10}"
                    )
                else:
                    print("Product not found.")

            # UPDATE
            elif option == "4":
                name = get_valid_name()
                price = get_valid_float("New price: ")
                quantity = get_valid_int("New quantity: ")

                success = update_product_csv(
                    name, {"price": price, "quantity": quantity}
                )

                print(
                    "\n✔ Product updated successfully."
                    if success
                    else "Product not found."
                )

            # DELETE
            elif option == "5":
                name = get_valid_name()

                success = delete_product_csv(name)

                print(
                    "\n✔ Product deleted successfully."
                    if success
                    else "Product not found."
                )

            # STATISTICS
            elif option == "6":
                products = read_products_csv()
                stats = calculate_statistics(products)

                if stats:
                    print("\n--- STATISTICS ---")
                    print(f"Total units: {stats['total_units']}")
                    print(f"Total value: ${stats['total_value']:.2f}")
                    print(
                        f"Most expensive: {stats['most_expensive'][0]} (${stats['most_expensive'][1]:.2f})"
                    )
                    print(
                        f"Highest stock: {stats['highest_stock'][0]} ({stats['highest_stock'][1]} units)"
                    )
                else:
                    print("Inventory is empty.")

            # SAVE
            elif option == "7":
                products = read_products_csv()

                if not products:
                    print("Inventory is empty. Nothing to save.")
                else:
                    ruta = input("Enter file path (e.g., data/export.csv): ").strip()

                    if not ruta:
                        print("Invalid path.")
                        continue

                    if not ruta.endswith(".csv"):
                        print("File must have .csv extension.")
                        continue

                    invalid_chars = ["<", ">", ":", '"', "|", "?", "*"]
                    if any(char in ruta for char in invalid_chars):
                        print("Invalid characters in file path.")
                        continue

                    directory = os.path.dirname(ruta)
                    if directory and not os.path.exists(directory):
                        print("Directory does not exist.")
                        continue

                    save_csv(products, ruta)

            # LOAD (
            elif option == "8":
                path = input(
                    "Enter CSV file path (e.g., data/inventario.csv): "
                ).strip()

                if not path:
                    print("Invalid path.")
                    continue

                if not path.endswith(".csv"):
                    print("File must have .csv extension.")
                    continue

                new_products, invalid_count = load_csv(path)

                if not new_products:
                    print("No valid products loaded.")
                    continue

                decision = input("Overwrite current inventory? (Y/N): ").strip().upper()
                current_products = read_products_csv()

                if decision == "Y":
                    save_csv(new_products, "data/data.csv")
                    action = "replaced"

                elif decision == "N":
                    merged = current_products.copy()

                    for new in new_products:
                        existing = search_product(merged, new["name"])

                        if existing:
                            existing["quantity"] += new["quantity"]
                            existing["price"] = new["price"]
                        else:
                            merged.append(new)

                    save_csv(merged, "data/data.csv")
                    action = "merged"

                else:
                    print("Invalid option.")
                    continue

                print("\n--- LOAD SUMMARY ---")
                print(f"Products loaded: {len(new_products)}")
                print(f"Invalid rows skipped: {invalid_count}")
                print(f"Action: {action}")

            # EXIT
            elif option == "9":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose between 1 and 9.")

        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Returning to menu...")
