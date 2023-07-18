#13. Area of a Circle
pi = 3.14
def areaOfCircle(radius):
    area=pi* pow(radius,2)
    return area
r = int(input("Enter the Radius of Circle: "))
area = areaOfCircle(r)
print("Area =",area)