#CIA system
from random import randint

def generate_numbers(): # function to generate random numbers i and j
    global i  
    global j
    i = randint(1,9)
    j = randint(1,9)
    main()
    

def main():
    while True:
        try:
            answer = int(input(f"How much is {i} times {j}: ")) #generate the questions for user to input the answers
            break
        except ValueError:
            print("Invalid. Enter an integer")
    response(answer)

def response(answer): # a function to give responses to user input
    if answer == (i * j):
        print("Very good!")
        generate_numbers() # called when user input is correct
    else:
        print("No. Please try again")
        main() #called when user input is wrong to ask the user the same question again
    




if __name__ == "__main__":
    generate_numbers() #only called if the condition is true 
