#progam that receives a string and remove duplicates
def main(): 
    text = input("Enter any string: ") #Get the string from the user input

    print(remove_duplicate(text))

def remove_duplicate(text):
    lst = []    #create an empty list
    for char in text:     #loop through each character in the string 
        if char not in lst:  
            lst.append(char) #and for every unique character you append it to the list
    
    result = "".join(lst) #joins the items in the list into one string
    return result
if __name__ == "__main__":
    main()
