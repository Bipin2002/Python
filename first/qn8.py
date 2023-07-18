#8. Percentage of 5 Subjects
a = int(input("enter your marks of math: "))
b = int(input("enter your marks of english: "))
c = int(input("enter your marks of science: "))
d = int(input("enter your marks of nepali: "))
e = int(input("enter your marks of social: "))
marks=[a,b,c,d,e]
def calculatepercentage(subjects):
    total_marks = 500 
    marks = sum(subjects)
    percentage = (marks / total_marks) * 100
    return percentage
percentage = calculatepercentage(marks)
print(percentage,"%")