# Lists
expenses = [250, 500, 150, 800, 200]
expenses.append(300)

print(expenses)
print("1st Element: " + str(expenses[0]))
print("Last Element: " + str(expenses[-1]))
print("No. of Elements: " + str(len(expenses)))

expenses.remove(200)
expenses.pop(0)
print("Final list of Expenses: ", expenses)

expenses.insert(2, 180)
print(f"List: {expenses}")
