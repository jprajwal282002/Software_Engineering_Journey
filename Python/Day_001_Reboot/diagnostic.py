expenses = [250, 500, 150, 800, 200, 450]
total = 0

for expense in expenses:
    print(expense)

for expense in expenses:
     total += expense

print (f"Total Expenses are: {total}")

count = 0

for i in expenses:
    if i >= 400:
        count += 1

print(f"Expenses >= 400: {count}")

category_expenses = {
    "Food": 400,
    "Travel": 700,
    "Shopping": 800
}

for key, value in category_expenses.items():
    print(key, value)

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total #return gives a value back to the code that called the function.

result = calculate_total(expenses)

print(result)


largest = expenses[0]

for expense in expenses:
    if expense > largest:
        largest = expense

print (largest)