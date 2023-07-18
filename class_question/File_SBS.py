import random

def initial_display():
    display = '''-------------------------------------------------
        Sunway Bhatbhatini System
           Maitidevi, Kathmandu
-------------------------------------------------'''
    return display


def input_info():
    name = input('Enter the name: ')
    id = random.randint(1000, 9999)
    address = input('Enter the Address: ')
    num_item = int(input('Enter Item purchased: '))
    item_price = []
    quantity_item = []
    total_price = []
    for i in range(num_item):
        item_prices = int(input(f'Enter {i+1} item unit price (Rs): '))
        quantity = int(input(f'Enter quantity of {i+1} item: '))
        item_price_quantity = item_prices * quantity
        item_price.append(item_prices)
        quantity_item.append(quantity)
        total_price.append(item_price_quantity)
    return name, id, address, num_item, item_price, quantity_item, total_price


def bill():
    total = sum(total_price)

    if total <= 500:
        discount = 1
        discount_amount = total * 0.01
        amount_after_d = total - discount_amount
    elif total > 500 and total <= 1000:
        discount = 3
        discount_amount = 500 * 0.01 + (total - 500) * 0.03
        amount_after_d = total - discount_amount
    elif total > 1000 and total <= 1500:
        discount = 5
        discount_amount = 500 * 0.01 + \
            (1000 - 500) * 0.03 + (total - 1000) * 0.05
        amount_after_d = total - discount_amount
    elif total > 1500 and total <= 2000:
        discount = 8
        discount_amount = 500 * 0.01 + \
            (1000 - 500) * 0.03 + (1500 - 1000) * 0.05 + (total - 1500) * 0.08
        amount_after_d = total - discount_amount
    else:
        discount = 10
        discount_amount = 500 * 0.01 + \
            (1000 - 500) * 0.03 + (1500 - 1000) * 0.05 + \
            (2000 - 1500) * 0.08 + (total - 2000) * 0.1
        amount_after_d = total - discount_amount
    return total, discount, discount_amount, amount_after_d


def value_print():
    a = f'''Customer name: {name}
Id no. : A{id}
Customer Address: {address}
-------------------------------------------------
|Item price \t|Quantity \t\t|Total Amount\t|
-------------------------------------------------\n'''
    b = ''
    for i in range(num_item):
        b += f'| {item_price[i]} \t\t\t| {quantity_item[i]} \t\t\t| {total_price[i]} \t\t\t|\n'
    c = f'''-------------------------------------------------
Mr/Mrs. {name}, you have purchased {num_item} items whose
total price is {total} and discount is {discount_amount} with
discount rate {discount}%, After discount amount is {amount_after_d}
-------------------------------------------------\n'''
    return a, b, c


with open('C:/Users/bipin nagarkoti/OneDrive/Desktop/5th sem/PYTHON/class_question/printdata.txt', 'w', encoding='utf-8') as f:
    f.write(initial_display() + '\n')
    name, id, address, num_item, item_price, quantity_item, total_price = input_info()
    total, discount, discount_amount, amount_after_d = bill()
    a, b, c = value_print()
    f.write(a)
    f.write(b)
    f.write(c)
