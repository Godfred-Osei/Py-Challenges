from random import randint
from sys import exit
count = 0
count_right = 0


def generate_numbers(): #function to generate numbers for multiplication
    global i
    global j
    i = randint(1,9)
    j = randint(1,9)
    main()

def message(count_right): #a function to handle the percentage and appropriate message to be displayed after count reach 10
    if ((count_right/10) * 100) > 75:
        exit("Congratulations you are ready to go to the next level")
    else:
        exit("Please ask your teacher for help")
        
    

def main():
    global count
    
    while True:
        try:
            answer = int(input(f"How much is {i} times {j}: ")) #generate the questions for user to input the answers
            count = count + 1
            break
        except ValueError:
            print("Invalid. Enter an integer")
    if count == 10: 
        message(count_right) 
    else:
        response(answer) #called while count is less than 10
    


def response(answer):
    global count_right
    global count_wrong

    num = randint(1,4) #generate numbers to randomize the responses
    
    if answer == (i * j):
        count_right = count_right + 1
        responses = {   
            1: "Very good!",
            2: "Excellent",
            3: "Nice work",
            4: "keep up the good work!"
            }
        print(responses[num])
        generate_numbers()


    else:
        responses = {
            1: "No. Please try again.",
            2: "Wrong. Try once more.",
            3: "Don't give up!",
            4: "No keep trying!"
            }
        print(responses[num])
        generate_numbers()
        

if __name__ == "__main__":
    generate_numbers()



