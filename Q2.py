#Q2 - Corrections to the initial codes
 
items_dict = {'a' : 239.99, 'b': 129.75, 'c' : 99.95, 'd' : 350.89} #dictionary for each item and its value
n = int(input("Enter the number of items you want to buy: "))

total_cost = 0
while n > 0:
    try:
        item = input("Kind of item sold: ").lower() #Get user input for the kind of item and returns a lower case of the user input
        quantity = int(input("Number of items sold: ")) #Get user input for the quantity of items
        quantityCost = items_dict[item] * quantity #Calculate the total cost of the item
        total_cost = total_cost + quantityCost
        payPerWeek = 200 + (9/100 * total_cost) #calculate the salary of the worker 
    except KeyError and ValueError:
        print("The items are either a, b, c or d.", "Enter an integer")
    n = n -1

print(f"Your pay for this week is ${payPerWeek: 0.4f}")