#Q6
from collections import Counter
shop1 =  Counter({
    'mango' : 20,
    'banana' : 30.4,
    'apple' : 15.40,
    'orange' : 40.12
} )

shop2 = Counter({
    'mango': 50,
    'banana': 26,
    'apple' : 35.71,
    'orange' : 15.78
})
# solution for a
print(f"The cost of 5 oranges from shop2 and 7 apples from shop 1 is {shop2['orange'] * 5  + shop1['apple']*7}")

#solution for b
shop1.update({'grapes': 14})
shop2.update({'grapes' : 17})
#print(shop1)
#print(shop2)

#solution for c
combined_dict = shop1 + shop2
print("final dictionary", str(combined_dict))
