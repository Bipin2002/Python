num = int(input("Enter the Length of fibonacci series: "))
def fibonacci_cal(num):
    num1 = 0
    num2 = 1
    next_number = 0
    list_num = []
    for _ in range(num):
        list_num.append(next_number)
        num1 = num2
        num2 = next_number
        next_number = num1 + num2
    print(list_num)
fibonacci_cal(num)
