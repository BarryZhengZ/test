class Customer:

   def __init__(self,cust_id,name,address,email,phone,memberstat):
       self.__cust_id = cust_id
       self.__name = name
       self.__address = address
       self.__email = email
       self.__phone = phone
       self.__memberstat = memberstat


   def get_customerid(self):
       return self.__cust_id
   def get_name(self):
       return self.__name
   def get_address(self):
       return self.__address
   def get_email(self):
       return self.__email
   def get_phone(self):
       return self.__phone
   def get_memberstat(self):
       return self.__memberstat
  
class Transaction:
   def __init__(self, date, item_name, cost, cust_id):
       self.__date = date
       self.__item_name = item_name
       self.__cost = cost
       self.__cust_id = cust_id
  
   def get_date(self):
       return self.__date
   def get_itemname(self):
       return self.__item_name
   def get_cost(self):
       return self.__cost
   def get_custid(self):
       return self.__cust_id

