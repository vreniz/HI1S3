# 📦 Inventory Management System (CSV-Based)

A console-based inventory management system developed in Python that allows users to perform CRUD operations and persist data using CSV files.

---

## 🚀 Features


- ✅ Full CRUD operations (Create, Read, Update, Delete)
- ✅ Clean and formatted console interface (table view)
- ✅ Color-coded feedback:
  - 🟢 Success messages  
  - 🔴 Error messages  
  - 🟡 Warnings  
- ✅ Inventory statistics:
  - Total units  
  - Total inventory value  
  - Most expensive product  
  - Product with highest stock  
  - Subtotal per product  
- ✅ CSV persistence (save & load)
- ✅ Smart CSV loading:
  - Overwrite or merge options  
  - Automatic conflict resolution  
- ✅ Strong input validation  
- ✅ Robust error handling (program never crashes)

---

## 🗂 Project Structure

```
project/
│
├── main.py        # User interface & interaction
├── crud.py        # Business logic (CRUD + statistics)
├── archive.py     # CSV handling (save/load + validation)
├── colors.py      # ANSI color management
└── data/
    └── data.csv   # Main persistent storage
```

---

## ⚙️ Requirements

- Python 3.10.12

---

## ▶️ How to Run

```bash
python3 main.py
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
Each product is represented as:

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

When loading a CSV file, the system prompts:
Overwrite current inventory? (Y/N)
### 🟥 Y → Overwrite 
* Replaces the entire inventory **Only valid rows are kept**
### 🟩 N → Merge 
* Combines existing and new data **If product already exists:**
  - Quantity is **summed** 
  - Price is **updated to the new value**

---

## ⚠️ Validations

* Header must be: **name,price,quantity.**
* Each row must contain exactly 3 values. 
* Price must be a valid float. 
* Quantity must be a valid integer. 
* No negative values allowed. 
* Invalid rows are skipped and counted.

---

## 📊 Example Output

```
-------------------------- INVENTORY --------------------------
#   Name                 Price      Quantity        Subtotal
-----------------------------------------------------------------
1   Cheese               $10.50     5          $52.50
2   Milk                 $5.50      3          $16.50
```

---
## 🎨 User Experience (UX) 
* Color-coded console output using ANSI escape codes. 
* Clear visual separation of sections.
* Pause between actions (Press ENTER to continue). 
* Structured tables for readability. 
---
## 🧠 Design Decisions 
* CSV chosen for simplicity and portability.
* Modular architecture: 
  * `crud.py` → logic 
  * `archive.py` → persistence 
  * `main.py` → UI 
* Centralized color handling for consistency. 
* Merge strategy prioritizes: 
  * Data preservation. 
  * Simplicity. 
--- 
## 🛡 Error Handling The system handles: 
* File not found. 
* Encoding errors. 
* Invalid CSV structure. 
* Invalid user input.
All errors are handled gracefully without stopping execution.
 ---
## 👩🏻‍💻 Author

**Vanessa Fontalvo Reniz** | Systems & Computer Engineer | Aspiring Software Developer.