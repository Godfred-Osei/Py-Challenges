import array
arr = []
n = 10
for x in range(n):
    x=int(input("enter the number: ")) #Get user inputs for the numbers
    arr.append(x) #add each number to an array
arr1 = sorted(arr) #sort the array in ascending order
for i in range(len(arr1)-1, 0, -1):
    print(f"The first two maximum numbers are {arr1[i-1]} and {arr1[i]}") #print the maximum two numbers
    break