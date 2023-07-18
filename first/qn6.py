#6. simple interest
p = float(input("Enter the Principle Rate "))
r = float(input("Enter the Intrest rate "))
t = float(input("Enter the time in years "))

def simpleinterest(p,r,t):
    si = (p*t*r)/100
    return si

s_interest = simpleinterest(p,r,t)
print(s_interest)