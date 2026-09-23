expenses = {
    ("Food", 250),
    ("Travel", 500),
    ("Food", 150),
    ("Shopping", 800),
    ("Travel", 200)
}


category_totals = {}

for category, amount in expenses:
        if category in category_totals:
         category_totals[category] += amount
        else: 
             category_totals[category] = amount
        print(category_totals)
 