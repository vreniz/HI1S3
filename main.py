# pylint: disable=wildcard-import
# pylint:disable=unused-wildcard-import
# pylint: disable=missing-function-docstring

from crud import *
from archive import *
import os
from colors import Colors


def pause():
    input(f"\n{Colors.YELLOW}Press ENTER to return to menu...{Colors.RESET}")


# ======================
# MENU
# ======================
def menu():
    print(f"\n{Colors.CYAN}{Colors.BOLD}=== INVENTORY SYSTEM ==={Colors.RESET}")
    print("1. Add product")
    print("2. Show products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")


# ======================
# NAME VALIDATION
# ======================
def get_valid_name():
    while True:
        name = input("Product name: ").strip()

        if not name:
            print(f"{Colors.RED}Name cannot be empty.{Colors.RESET}")
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
            print(
                f"{Colors.RED}Only letters, numbers and spaces are allowed.{Colors.RESET}"
            )
            continue

        if not has_letter:
            print(f"{Colors.RED}Name cannot be only numbers.{Colors.RESET}")
            continue

        return name


# ======================
# FLOAT VALIDATION
# ======================
def get_valid_float(message):
    while True:
        value = input(message).strip()

        if not value:
            print(f"{Colors.RED}Value cannot be empty.{Colors.RESET}")
            continue

        value = value.replace(",", ".")

        try:
            number = float(value)

            if number <= 0:
                print(f"{Colors.RED}Value must be greater than 0.{Colors.RESET}")
                continue

            return number

        except ValueError:
            print(
                f"{Colors.RED}Invalid number. Use format like 10.5 or 10,5{Colors.RESET}"
            )


# ======================
# INTEGER VALIDATION
# ======================
def get_valid_int(message):
    while True:
        value = input(message).strip()

        if not value:
            print(f"{Colors.RED}Value cannot be empty.{Colors.RESET}")
            continue

        if not value.isdigit():
            print(f"{Colors.RED}Only whole numbers allowed.{Colors.RESET}")
            continue

        number = int(value)

        if number <= 0:
            print(f"{Colors.RED}Value must be greater than 0.{Colors.RESET}")
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
                print(
                    f"{Colors.GREEN}✔ Product '{name}' added successfully.{Colors.RESET}"
                )
                pause()

            # SHOW
            elif option == "2":
                products = read_products_csv()

                if not products:
                    print(f"{Colors.YELLOW}Inventory is empty.{Colors.RESET}")
                else:
                    print(
                        f"\n{Colors.CYAN}{Colors.BOLD}--- INVENTORY ---{Colors.RESET}"
                    )
                    print(
                        f"{'#':<3} {'Name':<20} {'Price':<10} {'Quantity':<10} {'Subtotal':<10}"
                    )
                    print("-" * 65)

                    for i, p in enumerate(products, 1):
                        subtotal = p["price"] * p["quantity"]
                        print(
                            f"{i:<3} {p['name']:<20} ${p['price']:<9.2f} {p['quantity']:<10} ${subtotal:<9.2f}"
                        )

                pause()

            # SEARCH
            elif option == "3":
                name = get_valid_name()
                products = read_products_csv()

                result = search_product(products, name)

                if result:
                    print(f"\n{Colors.GREEN}--- PRODUCT FOUND ---{Colors.RESET}")
                    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10}")
                    print("-" * 40)
                    print(
                        f"{result['name']:<20} ${result['price']:<9.2f} {result['quantity']:<10}"
                    )
                else:
                    print(f"{Colors.RED}Product not found.{Colors.RESET}")

                pause()

            # UPDATE
            elif option == "4":
                name = get_valid_name()
                price = get_valid_float("New price: ")
                quantity = get_valid_int("New quantity: ")

                success = update_product_csv(
                    name, {"price": price, "quantity": quantity}
                )

                if success:
                    print(
                        f"{Colors.GREEN}✔ Product updated successfully.{Colors.RESET}"
                    )
                else:
                    print(f"{Colors.RED}Product not found.{Colors.RESET}")

                pause()

            # DELETE
            elif option == "5":
                name = get_valid_name()

                success = delete_product_csv(name)

                if success:
                    print(
                        f"{Colors.GREEN}✔ Product deleted successfully.{Colors.RESET}"
                    )
                else:
                    print(f"{Colors.RED}Product not found.{Colors.RESET}")

                pause()

            # STATISTICS
            elif option == "6":
                products = read_products_csv()
                stats = calculate_statistics(products)

                if stats:
                    print(
                        f"\n{Colors.CYAN}{Colors.BOLD}--- 📊 STATISTICS ---{Colors.RESET}"
                    )
                    print(
                        f"Total units: {Colors.GREEN}{stats['total_units']}{Colors.RESET}"
                    )
                    print(
                        f"Total value: {Colors.GREEN}${stats['total_value']:.2f}{Colors.RESET}"
                    )

                    print(
                        f"\n{Colors.YELLOW}Most expensive:{Colors.RESET} {stats['most_expensive'][0]} (${stats['most_expensive'][1]:.2f})"
                    )
                    print(
                        f"{Colors.YELLOW}Highest stock:{Colors.RESET} {stats['highest_stock'][0]} ({stats['highest_stock'][1]} units)"
                    )

                    subtotal = lambda p: p["price"] * p["quantity"]

                    print(
                        f"\n{Colors.CYAN}--- 📋 SUBTOTAL PER PRODUCT ---{Colors.RESET}"
                    )
                    print(
                        f"{'Name':<20} {'Price':<10} {'Quantity':<10} {'Subtotal':<10}"
                    )
                    print("-" * 65)

                    for p in products:
                        print(
                            f"{p['name']:<20} ${p['price']:<9.2f} {p['quantity']:<10} ${subtotal(p):<9.2f}"
                        )
                else:
                    print(f"{Colors.YELLOW}Inventory is empty.{Colors.RESET}")

                pause()

            # SAVE
            elif option == "7":
                products = read_products_csv()

                if not products:
                    print(
                        f"{Colors.YELLOW}Inventory is empty. Nothing to save.{Colors.RESET}"
                    )
                else:
                    ruta = input("Enter file path (e.g., data/export.csv): ").strip()

                    if not ruta:
                        print(f"{Colors.RED}Invalid path.{Colors.RESET}")
                        continue

                    if not ruta.endswith(".csv"):
                        print(
                            f"{Colors.RED}File must have .csv extension.{Colors.RESET}"
                        )
                        continue

                    invalid_chars = ["<", ">", ":", '"', "|", "?", "*"]
                    if any(char in ruta for char in invalid_chars):
                        print(
                            f"{Colors.RED}Invalid characters in file path.{Colors.RESET}"
                        )
                        continue

                    directory = os.path.dirname(ruta)
                    if directory and not os.path.exists(directory):
                        print(f"{Colors.RED}Directory does not exist.{Colors.RESET}")
                        continue

                    save_csv(products, ruta)
                    print(
                        f"{Colors.GREEN}✔ Inventory saved successfully.{Colors.RESET}"
                    )

                pause()

            # LOAD
            elif option == "8":
                path = input("Enter CSV file path (e.g., data/inventory.csv): ").strip()

                if not path:
                    print(f"{Colors.RED}Invalid path.{Colors.RESET}")
                    continue

                if not path.endswith(".csv"):
                    print(f"{Colors.RED}File must have .csv extension.{Colors.RESET}")
                    continue

                new_products, invalid_count = load_csv(path)

                if not new_products:
                    print(f"{Colors.RED}No valid products loaded.{Colors.RESET}")
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
                    print(f"{Colors.RED}Invalid option.{Colors.RESET}")
                    continue

                print(f"\n{Colors.GREEN}--- LOAD SUMMARY ---{Colors.RESET}")
                print(
                    f"{Colors.GREEN}✔ Products loaded:{Colors.RESET} {len(new_products)}"
                )
                print(
                    f"{Colors.RED}⚠ Invalid rows skipped:{Colors.RESET} {invalid_count}"
                )
                if action == "replaced":
                    print(f"{Colors.GREEN}🔄 Action:{Colors.RESET} Inventory replaced")
                else:
                    print(f"{Colors.CYAN}🔀 Action:{Colors.RESET} Inventory merged")

                pause()

            # EXIT
            elif option == "9":
                print(f"{Colors.GREEN}Goodbye!{Colors.RESET}")
                break

            else:
                print(
                    f"{Colors.RED}Invalid option. Please choose between 1 and 9.{Colors.RESET}"
                )

        except Exception as e:
            print(f"{Colors.RED}Unexpected error: {e}{Colors.RESET}")
            print(f"{Colors.YELLOW}Returning to menu...{Colors.RESET}")
