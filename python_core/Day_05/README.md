![Day 5 Banner](./d-5-1.png)

# Day 5 – Python Type Conversion

Welcome to **Day 5** of my **Python Zero to Advanced Journey**.  
Today’s focus was on **Python Type Conversion**, which is used to convert one data type into another to ensure calculations, comparisons, and program logic work correctly.

Type conversion is a core concept because **almost every program requires converting data types** at some point.

---

## 📌 Topics Covered Today

### 1️⃣ Implicit Type Conversion (Automatic)
- Python automatically converts smaller data types to larger ones when needed
- Ensures operations like `int + float` work without errors
- Examples:
  - `int + float` → float
  - `int + complex` → complex
  - `float + complex` → complex
  - `bool + int` → int (True = 1, False = 0)

### 2️⃣ Explicit Type Conversion (Manual)
- Programmer manually converts data types using built-in functions
- Ensures correct data types for calculations or input handling
- Common functions:
  - `int()`, `float()`, `str()`, `bool()`
  - `list()`, `tuple()`, `set()`
- Examples:
  - `int("10")` → 10
  - `float("15.5")` → 15.5
  - `str(100)` → '100'
  - `bool(0)` → False

---

## 🧠 Programs Written Today

### ✅ Program 1: Implicit Type Conversion
**Concepts used:**
- Automatic conversion
- Arithmetic operations

**What it does:**
- Demonstrates `int + float`, `int + complex`, and `bool + int`
- Shows resulting data types automatically converted

**Real-life use cases:**
- Calculators handling integers and decimals
- Automatic type adjustments in financial apps
- Game score calculations

---

### ✅ Program 2: Explicit Type Conversion
**Concepts used:**
- Manual conversion functions
- Data type control

**What it does:**
- Converts strings, floats, tuples, and integers manually
- Ensures operations work correctly without errors

**Real-life use cases:**
- Handling user input from forms
- Data parsing from files or APIs
- Converting database values for calculations

---

## 🎯 Learning Outcome

- Learned the difference between implicit and explicit conversion
- Understood how Python automatically handles numeric operations
- Practiced manually converting types to prevent errors
- Built a foundation for safe input handling and data manipulation

---

## 🔗 Author

**Agrojit**  
Python Learner | Daily Progress | Zero to Advanced
