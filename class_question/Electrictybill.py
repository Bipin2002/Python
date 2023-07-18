
def initial_display():
    print('''**************************************************************
                    Unicampus Electricity Bill                   
                        Putalisadak, Nepal                       
**************************************************************''')
    
def input_info():
    customers_info=[]
    num = int(input('Enter the number of customer: '))
    print()
    for i in range(num):
        customer_info = []
        print("**************************************************************")
        name = input("please Enter the name of the customer: ")
        address = input("Please enter the Address of the Customer: ")
        phone = input("Please enter the Phone number: ")
        unit = int(input("Please enter number of unit you consumed: "))
        customer_info.append(name)
        customer_info.append(address)
        customer_info.append(phone)
        customer_info.append(unit)
        customers_info.append(customer_info)
        print("**************************************************************")
        print()
    return num,customers_info

def bill_calculation(unit):
    if unit <= 80:
        amount = unit*4
        service_charge = 0
        d_amount = 0/100*amount
        total_service= amount+service_charge
        after_damount=total_service-d_amount

    elif unit > 80 and unit <= 150:
        amount = 80*4+(unit-80)*10
        service_charge= (((unit-80)*10)*5)/100
        d_amount = (((unit-80)*10)*5)/100
        total_service= amount+service_charge
        after_damount=total_service-d_amount

    elif unit > 150 and unit <= 250:
        amount = (80*4)+((150-80)*10)+(unit-150)*12
        d_amount = (((150-80)*10)*5)/100+(((unit-150)*12)*8)/100
        service_charge = (((150-80)*10)*5)/100+(((unit-150)*12)*5)/100
        total_service= amount+service_charge
        after_damount=total_service-d_amount

    elif unit > 250 and unit <= 350:
        amount = (80*4)+((150-80)*10)+((250-150)*12)+(unit-250)*15
        d_amount = (((150-80)*10)*5)/100+(((250-150)*12)*8)/100+(((unit-250)*15)*10)/100
        service_charge = (((150-80)*10)*5)/100+(((250-150)*12)*5)/100+(((unit-250)*15)*8)/100
        total_service= amount+service_charge
        after_damount=total_service-d_amount

    elif unit > 350 and unit <= 500:
        amount = (80*4)+((150-80)*10)+((250-150)*12)+(350-250)*15+(unit-350)*18
        d_amount = (((150-80)*10)*5)/100+(((250-150)*12)*8)/100 +(((350-250)*15)*10)/100+(((unit-350)*18)*12)/100
        service_charge =(((150-80)*10)*5)/100+(((250-150)*12)*5)/100 +(((350-250)*15)*8)/100+(((unit-350)*18)*10)/100
        total_service= amount+service_charge
        after_damount=total_service-d_amount

    else:
        amount = (80*4)+((150-80)*10)+((250-150)*12) + (350-250)*15+(500-350)*18+(unit-500)*20
        d_amount = (((150-80)*10)*5)/100+(((250-150)*12)*8)/100+(((350-250)*15)* 10)/100+(((500-350)*18)*12)/100+(((unit-500)*20)*15)/100
        service_charge = (((150-80)*10)*5)/100+(((250-150)*12)*5)/100+(((350-250)*15)* 8)/100+(((500-350)*18)*10)/100+(((unit-500)*20)*12)/100
        total_service= amount+service_charge
        after_damount=total_service-d_amount
    
    return total_service,after_damount,service_charge,amount,d_amount

def print_value():
     for i in range(num): 
        total_service,after_damount,service_charge,amount,d_amount = bill_calculation(customers_info[i][3])  
        print(f'''**************************************************************
                Unicampus Electricity Bill                   
                        Putalisadak, Nepal                       
**************************************************************
Customer Name:",{customers_info[i][0]}\tCustomer Address:{customers_info[i][1]}
Phone:{customers_info[i][2]} \t\t Unit Consumed:{customers_info[i][3]}
Bill Amount: {amount}\t\tSercice Charge",service_charge
Total Amount:{total_service}\t\tTotal discount:{d_amount}
After Discount Amount: {after_damount}
Your total bill is:{amount}+{service_charge} Mr/Mrs. {customers_info[i][0]}. Your discount  price is \n Rs.{d_amount} and After discount amount is Rs.{after_damount}.
**************************************************************
''')
        
num,customers_info = input_info()
print_value()