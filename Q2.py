#Q2
items_dict = {'a' : 239.99, 'b': 129.75, 'c' : 99.95, 'd' : 350.89} #dictionary for each item and its value

item = input("Kind of item sold: ") #Get user input for the kind of item
quantity = int(input("Number of items sold: ")) #Get user input for the quantity of items
quantityCost = items_dict[item] * quantity #Calculate the total cost of the item
payPerWeek = 200 + (9/100 * quantityCost) #calculate the salary of the worker 
print(f"Your pay for this week is ${payPerWeek} ")