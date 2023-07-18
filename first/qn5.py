#5. Convert a Person’s Name in Abbreviated 
firstname = input("Enter your first name")
sername = input("Enter your sername")
def abbreviate_name(fName,sName):
    a = fName[:1]
    b = sName[:1]
    return a+b
abbreviated_code = abbreviate_name(firstname,sername)
print(abbreviated_code) 
