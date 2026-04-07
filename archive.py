import csv
from colors import Colors


def save_csv(inventario, ruta, incluir_header=True):
    """Save inventory to CSV file"""
    if not inventario:
        print(f"{Colors.YELLOW}Inventory is empty. Nothing to save.{Colors.RESET}")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if incluir_header:
                writer.writerow(["name", "price", "quantity"])

            for p in inventario:
                writer.writerow([p["name"], p["price"], p["quantity"]])

        print(f"{Colors.GREEN}✔ Inventory saved in:{Colors.RESET} {ruta}")

    except PermissionError:
        print(f"{Colors.RED}Permission denied. Cannot write file.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}Error saving file: {e}{Colors.RESET}")


def load_csv(path):
    """
    Load inventory from CSV with validation.
    Returns: (products_list, invalid_rows_count)
    """
    products = []
    invalid_rows = 0

    try:
        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)

            header = next(reader, None)

            if header != ["name", "price", "quantity"]:
                print(
                    f"{Colors.RED}Invalid CSV header. Expected: name,price,quantity{Colors.RESET}"
                )
                return [], 0

            for row in reader:
                if len(row) != 3:
                    invalid_rows += 1
                    continue

                name, price, quantity = row

                try:
                    price = float(price)
                    quantity = int(quantity)

                    if price < 0 or quantity < 0:
                        raise ValueError

                    products.append(
                        {"name": name, "price": price, "quantity": quantity}
                    )

                except ValueError:
                    invalid_rows += 1

        # ✅ mensaje positivo opcional
        print(f"{Colors.GREEN}✔ File loaded successfully.{Colors.RESET}")

        return products, invalid_rows

    except FileNotFoundError:
        print(f"{Colors.RED}File not found.{Colors.RESET}")
    except UnicodeDecodeError:
        print(f"{Colors.RED}Encoding error.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}Unexpected error: {e}{Colors.RESET}")

    return [], 0
