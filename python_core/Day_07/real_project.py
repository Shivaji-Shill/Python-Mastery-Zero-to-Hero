# Real Project: Monthly Expense Tracker
""" Project Goal: 
1. List of monthly expenses
2. Total Calculate
3. Average expense"""

# List of monthly expenses
expenses = [5000, 3000, 2500, 4000, 1500]

total = 0 # Store total expense

# Loop through expenses to calculate total
for cost in expenses:
    total += cost

# Calculate average enpense
average = total / len(expenses)

print("Monthly Expenses:", expenses)
print("Total Expense:", total)
print("Average Expense:", average)
