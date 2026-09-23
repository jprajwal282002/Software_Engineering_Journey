# for loop
expenses = [250, 350, 800, 950, 630]
total = 0

for expense in expenses: 
    total += expense

print(f"Total Expense: {total}")

count = 0

for expense in expenses:
    if expense >= 400:
        print(expense)
        count += 1

print(count)