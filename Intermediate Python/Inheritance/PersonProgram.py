import PersonClass as p
name = "John"
address = "1234 Main St"
phone_number = "123-456-7890"
cust_number = 1234
on_list_flag = True


person1 = p.Person(name,address,phone_number)


customer1 = p.Customer(name,address,phone_number,cust_number,on_list_flag)


person1.print_person()


print()
print()
print()


customer1.print_person()

