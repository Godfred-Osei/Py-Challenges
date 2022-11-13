def main():
    weight = float(input("What's your weight in pounds: ")) #Get the weight of the person in pounds

    height = float(input("What's your height in inches: ")) #Get the height of the person in inches

    BMI = (weight * 703)/(height * height) #Calculate the BMI of the person using the formula
    BMI = round(BMI,1)
    print(f"Your BMI is: {BMI}")
    outcome(BMI)

def outcome(x):
    if x < 18.5:
        print("Underweight")
    elif x > 18.5 and x < 24.9:
        print("Normal")
    elif x > 24.9 and x < 29.9: 
        print("Overweight")
    else:
        print("Obese")

main()
