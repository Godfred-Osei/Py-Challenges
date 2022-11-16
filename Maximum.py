arr = []
n = 10
index = 0
for x in range(n):
    x=int(input(f"Enter the number, index: {index}: ")) #Get user inputs for the numbers
    arr.append(x) #add each number to an array
    index = index + 1
arr1 = sorted(arr) #sort the array in ascending order

print(f"The first two maximum numbers are {arr1[n-1]} and {arr1[n-2]}") #print the maximum two numbers