#guessing game
from random import randint 
from sys import exit

count = 0 #initialising count to zero 
#the analogy is that count will be increased by one whenever main function is called so that the number of guesses can be counted 

def generate_number(): 
    global x
    x = randint(1,1000) #generate a random number between 1 and 1000
    main()



def main():
    global count 
    count = count + 1
    while True:
        try:
            guess = int(input("Guess a number between 1 and 1000: "))
            if guess < 0:
                guess = int(input("Guess a number between 1 and 1000: "))
            break
        except ValueError:
            pass
    

    guess_number(guess)


def guess_number(guess):
    while True:
        if guess > x:
            print("Too high. Try again")
            main()
        elif guess < x:
            print("Too low. Try again")
            main()
        else: 
            print("Congratulations. You guessed the number!")
            break


    if count < 10:
        print("You know the secret and you got lucky!")
    elif count == 10:
        print("Aha! You know the secret!")
    else:
        print("You should do better!")
    
    choice = input("Do you want to play again? Yes/No : ").lower()
    if choice == 'yes':
        generate_number()
    else: 
        exit()
    
if __name__ == "__main__":
    generate_number()