
num =int(input("Enter number:"))
def palinderome(num):
    temp=num
    rev=0
    while(num>0):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return temp,rev
temp,rev= palinderome(num)
if(temp==rev):
    print(f"{temp} is a palindrome number.")
else:
    print(f"{temp} is not a palindrome number.")