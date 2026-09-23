student = {
    "name" : "Prajwal",
    "course" : "MCA",
    "city" : "Pune"
}

#print(student["name"])
#print(student["city"])
#student["semseter"] = 3
#student["city"] = "Mumbai"

#print(student.get("age"))

#for key in student:
 #   print(key)

#for key, value in student.items():
 #   print(key, value)

#expense = {
 #   "category" : "food",
  #  "amount" : 250,
   # "payment_method" : "online"
#}

#print(expense["category"])
#print(expense["amount"])

expenses = {
    "Food" : 400,
    "Travel" : 700,
    "Shopping" : 800
}

total = 0

for key, value in expenses.items():
    total += value
    print(key, " : ", value)
print(total)