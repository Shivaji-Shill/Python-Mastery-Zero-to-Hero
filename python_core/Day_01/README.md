# Day 1 – User Input & Basic Calculation

![Day 1 Banner](./banner_day01.png)
![Day 1 Banner](./banner_day1.png)
---

## 🚀 What We Learned Today

1. **User Input**
   - Learned to take input from the user using `input()` function.
   - Input always returns a **string**, so conversion may be needed for calculations.

2. **String → Number Conversion**
   - Converted age input (string) to integer using `int()` to perform arithmetic.
   - Converted calculation results back to string using `str()` for combining with text.

3. **Basic Arithmetic**
   - Sum, Difference, Product, Division of two numbers.
   - Practiced combining user input with calculations.

4. **Backend Mindset**
   - Input → Process → Output workflow.
   - Understanding type conversion is essential for real backend programming.

---

## ⚠️ Issues & Notes While Running Code

- **VS Code Terminal**
  - To run the code, make sure to **run it in the terminal**.
  - If you try to run `input()` in the “Run Code” button or Output window, it may not accept user input.
  - Correct way: **Open Terminal → Run: `python 01_user_input_calculation.py`**.
  
- **Type Errors**
  - Adding string + number directly will cause **TypeError**.
  - Always convert number → string using `str()` before combining with text.
  
- **Division**
  - `/` always gives float result in Python.
  - Use `//` if you want integer division.

---

## 📂 Code Files

- `01_user_input_calculation.py` → Contains all the Day 1 examples:
  - Name input & greeting
  - Age input & next year calculation
  - Two numbers arithmetic
  - All with comments in English + Bangla explanations

---

## 💡 Tips

- Practice **step by step** in VS Code terminal.
- Always check **variable types** using `type()` if unsure.
- This workflow prepares you for **backend logic**:
  - Taking input from user → Processing data → Outputting result.
