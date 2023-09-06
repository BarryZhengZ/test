class Person:
   def __init__(self,name,address,number):
       self.name = name
       self.address = address
       self.number = number
   def get_name(self):
       return self.name
   def get_address(self):
       return self.address
   def get_phone(self):
       return self.number


   def print_person(self):
       print("Name:",self.name)
       print("Address:",self.address)
       print("Phone:",self.number)


class Customer(Person):
   def __init__(self,name,address,number,cust_number,wish_mail_list):
       Person.__init__(self,name,address,number)
       self.__cust_number = cust_number
       self.__wish_mail_list = wish_mail_list


   def print_person(self):
       print("Method 1")
       Person.print_person(self)
       print("Customer Number:", self.__cust_number)
       if self.__wish_mail_list:
           print("On mailing list: Yes")
       else:
           print("On mailing list: No")


       print("Method 2")
       print(f"Name: {Person.get_name(self)}")
       print(f"Address: {Person.get_address(self)}")
       print(f"Phone: {Person.get_phone(self)}")
       print(f"Customer number: {self.__cust_number}")
       if self.__wish_mail_list:
           print("On mailing list: Yes")
       else:
           print("On mailing list: No")

