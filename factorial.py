def main():
    num = int(input("Enter the number to compute its factorial: ")) #Get user input 
    print(f"The factorial of {num} is {factorial(num)} ") #Print the factorial of the number
    
def factorial(x):
    if x < 2: 
        return 1
    else:
        return x * factorial(x-1) # a recursive function to calculate the the factorial of the number
main()