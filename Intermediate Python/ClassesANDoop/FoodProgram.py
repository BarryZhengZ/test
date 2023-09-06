import FoodClass as fc

cust_id = 570
name = "Danni Sellyar"
address = "97 Mitchell Way Hewitt Texas 76712"
email = "dsellyarft@gmpg.org"
phone = "254-555-9362"
memberstat = False
customer = fc.Customer(cust_id,name,address,email,phone,memberstat)


# cust_id = "569"
# name = "Aubree Himsworth"
# address = "1172 Moulton Hill Waco Texas 76710"
# email = "ahimsworthfs@list-manage.com"
# phone = "254-555-2273"
# memberstat = True
# customer = fc.Customer(cust_id,name,address,email,phone,memberstat)

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
               'trans2':['2/15/2023','The Octobreakfast',18,569],
               'trans3':['2/15/2023','The Octoveg',16,570],
               'trans4':['2/15/2023','The Octoburger',20,570],
}

ordertotal = 0
items = []

for transaction in dict.items():
   if transaction[1][3] == int(customer.get_customerid()):
       items.append({"item": transaction[1][1], "cost": transaction[1][2]})
       ordertotal += transaction[1][2]


if customer.get_memberstat() == True:
   memberdiscount = ordertotal * 0.2
   costafterdiscount = ordertotal - memberdiscount

print("Customer Name: ", customer.get_name)
print("Phone: ", customer.get_phone)
for item in items:
   print("Order Item: " + item['item'] + " Price: $" + format(item['cost'],'.2f'))
print("Total Cost: $" + format(ordertotal,'.2f'))
if memberstat == True:
   print("Member Discount: $" + format(memberdiscount,'.2f'))
   print("Total Cost after Discount: $" + format(costafterdiscount,'.2f'))









