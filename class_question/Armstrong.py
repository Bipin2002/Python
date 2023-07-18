num = int(input('Enter the Number: '))
def armstrong_num(num):
    sum = 0
    temp = num
    length = len(str(num))
    for i in range(length):
        digit = temp % 10
        sum += digit ** length
        temp //=  10
    return sum
sum = armstrong_num(num)
if num == sum:
   print(f"{num} is an Armstrong number")
else:
   print(f"{num} is not an Armstrong number")