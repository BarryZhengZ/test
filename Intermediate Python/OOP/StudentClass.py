from datetime import date
class Student:


   def __init__(self,student_id,n,dob,c):
       self.__StudentID = student_id
       self.__Name = n
       self.__dob = dob
       self.__classification = c
       self.__age = 0
       self.__register = ""


   def cal_age(self):
       today = date.today()
       dob = self.__dob.split('/')
       dob_year = dob[2]
       self.__age = today.year - int(dob_year)


   def cal_classification(self):
       if self.__classification == "Freshman":
           self.__register =  "4/10 thru 4/12"
       elif self.__classification == "Sophomore":
           self.__register = "4/7 thru 4/9"
       elif self.__classification == "Junior":
           self.__register = "4/4 thru 4/6"
       elif self.__classification == "Senior":
           self.__register = "4/1 thru 4/3"
       else:
           self.__register = "classification not found..."


   def get_age(self):
       return self.__age
  
   def get_registration(self):
       return self.__register


  



