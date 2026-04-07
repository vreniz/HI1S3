import csv
import os

DATA_CSV = os.path.join("data", "data.csv")


# ======================
# CREATE
# ======================
def create_product_csv(product):
    file_exists = os.path.isfile(DATA_CSV)

    try:
        with open(DATA_CSV, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])

            if not file_exists:
                writer.writeheader()

            writer.writerow(product)

    except Exception as e:
        print(f"Error writing CSV: {e}")


# ======================
# READ
# ======================
def read_products_csv():
    if not os.path.isfile(DATA_CSV):
        return []

    try:
        with open(DATA_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            products = []

            for row in reader:
                try:
                    row["price"] = float(row["price"])
                    row["quantity"] = int(row["quantity"])
                    products.append(row)
                except:
                    continue

            return products

    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []


# ======================
# UPDATE
# ======================
def update_product_csv(name, new_data):
    products = read_products_csv()
    updated = False

    for p in products:
        if p["name"].lower() == name.lower():
            p.update(new_data)
            updated = True

    if updated:
        try:
            with open(DATA_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
                writer.writeheader()
                writer.writerows(products)
        except Exception as e:
            print(f"Error updating CSV: {e}")

    return updated


# ======================
# DELETE
# ======================
def delete_product_csv(name):
    products = read_products_csv()
    new_products = [p for p in products if p["name"].lower() != name.lower()]

    if len(new_products) != len(products):
        try:
            with open(DATA_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
                writer.writeheader()
                writer.writerows(new_products)
            return True
        except Exception as e:
            print(f"Error deleting product: {e}")

    return False


# ======================
# SEARCH
# ======================
def search_product(products, name):
    for p in products:
        if p["name"].lower() == name.lower():
            return p
    return None


# ======================
# STATISTICS
# ======================
def calculate_statistics(products):
    if not products:
        return None

    total_units = sum(p["quantity"] for p in products)
    total_value = sum(p["price"] * p["quantity"] for p in products)

    most_expensive = max(products, key=lambda p: p["price"])
    highest_stock = max(products, key=lambda p: p["quantity"])

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": (most_expensive["name"], most_expensive["price"]),
        "highest_stock": (highest_stock["name"], highest_stock["quantity"]),
    }
