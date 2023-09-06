import StudentClass as sc


studentid = 1001
name = 'John'
dob = '10/11/2001'
classification = 'Junior'


student1 = sc.Student(studentid, name, dob, classification)


student1.cal_age()
student1.cal_classification()


print(f"Student age is: {student1.get_age()}")
print(f"Student can register between {student1.get_registration()}")







