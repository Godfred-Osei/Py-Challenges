#CIA system
from random import randint

def generate_numbers():
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

def response(answer):

    num = randint(1,4)

    if answer == (i * j):
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
        main()

if __name__ == "__main__":
    generate_numbers()
        
        
