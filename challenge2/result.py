def main():
    num = int(input("Enter the number: ")) #get the number from the user
    arrayA = [21,4,9,8,13,40,32,18,27,31,11,29,33,37,41] #get array from the user
    print(check(arrayA, num))
    



def check(arrayA, n):
    i = 0
    result = []
    while i < len(arrayA): 
        if (arrayA[i] % n) == 0:
            result.append(arrayA[i])
        i = i + 1
    return result

if __name__ == "__main__":
    main()
