#7. Gross Salary of an Employee 
basic_salary = int(input ("Enter your basic_salary "))
allowances= int(input("Enter your allowances "))
bonus = int(input("Enter your Bonus "))

def calculate_gross_salary(basic_salary, allowances, bonus):
    gross_salary = basic_salary + allowances + bonus
    return gross_salary

gross_salary = calculate_gross_salary(basic_salary, allowances, bonus)
print("Gross Salary =", gross_salary)
