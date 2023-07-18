#4. Area of Triangle 
import math
a = int (input("Enter the First Side ="))
b = int (input("Enter the Second Side ="))
c = int (input("Enter the Third Side ="))
s=(a+b+c)/2
def areaofTriangle(a,b,c,s):
    area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
area = areaofTriangle(a,b,c,s)
print("Area of Triangle is ",area)