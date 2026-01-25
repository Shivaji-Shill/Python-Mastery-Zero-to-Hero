# Categorized expenses (using tuple for fixed categories)
categorise = ("Rent", "Food", "Internet", "Transport", "Other")
expenses = [8000, 4000, 1200, 1500, 2300]

total = sum(expenses)

print("Category wise expenses:")

for i in range(len(categorise)):
    print(categorise[i], ":", expenses[i])

print("Total Monthly Cost:", total)