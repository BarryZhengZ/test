#------------------------------------------------------------
#Name: Zhang, Zheng
#MIS 3301 – Spring,2022 
#Purpose: Order Receipt Generator
#File: Ch2-HW1-OrderReceiptGenerator.py
#------------------------------------------------------------


#Constants
tax_rate = 0.0825
tip_percent = 0.2

#Input
product_name_1 = input('Enter item #1 name: ')
product_price_1 = float(input('Enter item #1 price: '))
print()
product_name_2 = input('Enter item #2 name: ')
product_price_2 = float(input('Enter item #2 price: '))

#Process
subtotal = product_price_1 + product_price_2
tax = subtotal * tax_rate
total = subtotal + tax
tip = total * tip_percent
grand_total = total + tip

#Output
print('\n' * 2)
print('''Victorino's Country Kitchen''')
print('Developer: Zhang, Zheng')
print('*' * 30)
print(format(product_name_1,'20') + format(product_price_1,'10'))
print(format(product_name_2,'20') + format(product_price_2,'10'))
print(format(' ','20') + format('------','>10'))
print(format('Subtotal','20') + format(subtotal,'10,.2f'))
print(format('Tax','20') + format(tax,'10,.2f'))
print(format('Total','20') + format(total,'10,.2f'))
print(format('Tip (20%)','20') + format(tip,'10,.2f'))
print(format(' ','20') + format('------','>10'))
print(format('Grand Total','20') + format(grand_total,'10,.2f'))
