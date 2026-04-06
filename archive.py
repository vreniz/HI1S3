import csv


def save_csv(inventario, ruta, incluir_header=True):
    """Save inventory to CSV file"""

    if not inventario:
        print("Inventory is empty. Nothing to save.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if incluir_header:
                writer.writerow(["name", "price", "quantity"])

            for p in inventario:
                writer.writerow([p["name"], p["price"], p["quantity"]])

        print(f"Inventory saved in: {ruta}")

    except PermissionError:
        print("Permission denied. Cannot write file.")
    except Exception as e:
        print(f"Error saving file: {e}")


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

            # ✅ header validation
            if header != ["name", "price", "quantity"]:
                print("Invalid CSV header. Expected: name,price,quantity")
                return [], 0

            for row in reader:
                # ✅ must have 3 columns
                if len(row) != 3:
                    invalid_rows += 1
                    continue

                name, price, quantity = row

                try:
                    price = float(price)
                    quantity = int(quantity)

                    # ❌ no negatives
                    if price < 0 or quantity < 0:
                        raise ValueError

                    products.append(
                        {"name": name, "price": price, "quantity": quantity}
                    )

                except ValueError:
                    invalid_rows += 1

        return products, invalid_rows

    except FileNotFoundError:
        print("File not found.")
    except UnicodeDecodeError:
        print("Encoding error.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return [], 0
