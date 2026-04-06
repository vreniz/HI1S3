# 📦 Inventory Management System (CSV-Based)

A console-based inventory management system developed in Python that allows users to perform CRUD operations and persist data using CSV files.

---

## 🚀 Features

- ✅ Add, update, delete, and search products  
- ✅ Display inventory in a formatted table  
- ✅ Calculate statistics:  
  - Total units  
  - Total inventory value  
  - Most expensive product  
  - Product with highest stock  
- ✅ Save inventory to CSV  
- ✅ Load inventory from CSV with:
  - Validation  
  - Error handling  
  - Merge or overwrite options  
- ✅ Input validation (names, price, quantity)  
- ✅ Robust error handling (no crashes)  

---

## 🗂 Project Structure

```
project/
│
├── main.py
├── crud.py
├── archive.py
└── data/
    └── data.csv
```

---

## ⚙️ Requirements

- Python 3.x  

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📋 Menu Options

```
1. Add product
2. Show products
3. Search product
4. Update product
5. Delete product
6. Statistics
7. Save CSV
8. Load CSV
9. Exit
```

---

## 🧾 Data Structure

```python
{
  "name": str,
  "price": float,
  "quantity": int
}
```

---

## 💾 CSV Format

```csv
name,price,quantity
Cheese,10.5,5
Milk,5.5,3
```

---

## 🔄 Load CSV Behavior

Overwrite current inventory? (Y/N)

- Y → Replace  
- N → Merge  

---

## ⚠️ Validations

- Name: letters, numbers, spaces  
- Price: float > 0  
- Quantity: int > 0  

---

## 📊 Example Output

```
--- INVENTORY ---
#   Name                 Price      Quantity
--------------------------------------------------
1   Cheese               $10.50     5
2   Milk                 $5.50      3
```

---

## 👨‍💻 Author

Systems Engineering Project