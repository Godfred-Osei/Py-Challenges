#calculate the distance between two points

from math import sqrt

def main():
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))

    print(f"The distance is {calculate_distance(x1,y1,x2,y2): 0.2f}")

def calculate_distance(x1,y1,x2,y2):
    result = (x2-x1)**2 + (y2-y1)**2
    return sqrt(result)


if __name__ == "__main__":
    main()


