#check whether three numbers form triangle
import sys

def main():
    try:
        x = int(input("What's x? "))
        if x < 0:
             x = int(input("What's x? "))

        y = int(input("What's y? "))
        if y < 0:
            y = int(input("What's y? "))

        z = int(input("What's z? "))
        if z < 0:
            z = int(input("What's z? "))

    except ValueError:
        sys.exit("Enter an integer")


    print(check(x,y,z))

def check(x,y,z):
    if (x+y) > z and (x+z) > y and (y+z) > x:
        return True
    else: 
        return False

if __name__ == "__main__":
    main()
