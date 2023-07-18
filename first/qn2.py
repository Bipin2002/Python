#2. Area and Circumference of a Circle 
pi = 3.14
def areaOfCircle(radius):
    area=pi* pow(radius,2)
    return area
def circumstanceOfCircle(radius):
    cir = pi * radius
    return cir

r = int(input("Enter the Radius of Circle "))
area = areaOfCircle(r)
circumstance = circumstanceOfCircle(r)
print("Area =",area)
print("Circumstance =",circumstance)

