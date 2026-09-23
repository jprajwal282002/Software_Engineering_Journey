def is_large_expense(amount):
    if amount >= 1000:
        return True
    else:
        return False

amount = int(input("Enter the amount: "))
print(is_large_expense(amount))

print(type(amount))