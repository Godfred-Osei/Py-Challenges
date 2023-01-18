from random import randint

def addition(op):
    i = randint(1,10)
    j = randint(1,10)
    num = randint(1, 4)
    responses = {
            1: "Very good!",
            2: "Excellent",
            3: "Nice work",
            4: "keep up the good work!"
            }
    while True:
        try:
            answer = int(input(f"What's {i} plus {j}: "))
            break
        except ValueError: 
            print("Invalid Input")
    if (answer) == (i + j):
        print(responses[num])
    else:
        responses = {
            1: "No. Please try again.",
            2: "Wrong. Try once more.",
            3: "Don't give up!",
            4: "No keep trying!"
            }
        print(responses[num])
    if op == 5:  #condition to check the type of operation
        mixture()
    else:
        addition(op)

def subtraction(op):
    i = randint(1,10)
    j = randint(1,10)
    num = randint(1, 4)
    responses = {
            1: "Very good!",
            2: "Excellent",
            3: "Nice work",
            4: "keep up the good work!"
            }
    while True:
        try:
            answer = int(input(f"What's {i} minus {j}: "))
            break
        except ValueError: 
            print("Invalid Input")
    if (answer) == (i - j):
        print(responses[num])
    else:
        responses = {
            1: "No. Please try again.",
            2: "Wrong. Try once more.",
            3: "Don't give up!",
            4: "No keep trying!"
            }
        print(responses[num])
    if op == 5:    #condition to check the type of operation
        mixture()
    else:
        subtraction(op)
    

def multiplication(op):
    i = randint(1,10)
    j = randint(1,10)
    num = randint(1, 4)
    responses = {
            1: "Very good!",
            2: "Excellent",
            3: "Nice work",
            4: "keep up the good work!"
            }
    while True:
        try:
            answer = int(input(f"What's {i} multiplied by {j}: "))
            break
        except ValueError: 
            print("Invalid Input")
    if (answer) == (i*j):
        print(responses[num])
    else:
        responses = {
            1: "No. Please try again.",
            2: "Wrong. Try once more.",
            3: "Don't give up!",
            4: "No keep trying!"
            }
        print(responses[num])
    if op == 5:     #condition to check the type of operation
        mixture()
    else:
        multiplication(op)
    
def division(op):
    i = randint(1,10)
    j = randint(1,10)
    num = randint(1, 4)
    responses = {
            1: "Very good!",
            2: "Excellent",
            3: "Nice work",
            4: "keep up the good work!"
            }
    while True:
        try:
            answer = float(input(f"What's {i} divided {j}: "))
            break
        except ValueError: 
            print("Invalid Input")
    if answer == round((i/j),2):
        print(responses[num])
    else:
        responses = {
            1: "No. Please try again.",
            2: "Wrong. Try once more.",
            3: "Don't give up!",
            4: "No keep trying!"
                }
        print(responses[num])
    if op == 5:
        mixture()   #condition to check the type of operation
    else:
        division(op)
        
def mixture():  #function for the mixture and the op variable is always initialize to 5 when having mixtures
    op = 5
    n = randint(1,4)
    if n == 1:
        addition(op)
    elif n == 2:
        subtraction(op)
    elif n == 3:
        multiplication(op)
    elif n == 4:
        division(op)

def main(): #main function to get the type of operation
    global op
    print(
        "Enter 1 for Adddition, 2 for subtraction, 3 for division, 4 for multiplicaton and 5 for mixture: ")
    while True:
        try:
            op = int(input())
            break
        except ValueError:
            print("Invalid Input.")
    if op == 1:
        addition(op)
    elif op == 2:
        subtraction(op)
    elif op == 3:
        division(op)
    elif op == 4:
        multiplication(op)
    elif op == 5:
        mixture()

if __name__ == "__main__":
    main()
    
    

    


        