#3. Print Ascii Value of the Character 
charater = input("Enter the Charater ")
def asciivalue(char):
    ascii=ord(char)
    return ascii
value = asciivalue(charater)
print("The Ascii Value of ",charater," is ",value)