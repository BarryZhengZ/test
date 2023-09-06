''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num_list = list(filter(lambda num:num%2 == 0, original_list))
odd_num_list = list(filter(lambda num:num%2 == 1, original_list))
print(even_num_list)
print(odd_num_list)






''' 2)
find which days of the week have exactly 6 characters.
'''


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
new_list = list(filter(lambda length: len(length)==6,weekdays))
print(new_list)






''' 3)
remove specific words from a given list
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']


Remove words:
['orange', 'black']


After removing the specified words from the said list:
['red', 'green', 'blue', 'white']


'''
original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_list = ['orange','black']
final_list = list(filter(lambda n: n not in remove_list, original_list))
print(final_list)




''' 4)
remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]


Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
final_list = list(filter(lambda num: num not in list2,list1))
print(final_list)




''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]


'''
original_list = ['red', 'black', 'white', 'green', 'orange']
result1 = list(filter(lambda n: 'ack' in n, original_list))
print(result1)
result2 = list(filter(lambda i: 'abc' in i, original_list))
print(result2)




''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
str1 = "Hello8world"
uppercase = lambda x: any(y.isupper() for y in x)
lowercase = lambda x: any(y.islower() for y in x)
digit = lambda x: any(y.isdigit() for y in x)
valid_password = lambda x: len(x) >= 8 and uppercase(x) and lowercase(x) and digit(x)
if valid_password(str1):
   print("Valid Password.")
else:
   print("Invalid Password.")


str1 = "HELLO"
uppercase = lambda x: any(y.isupper() for y in x)
lowercase = lambda x: any(y.islower() for y in x)
digit = lambda x: any(y.isdigit() for y in x)
valid_password = lambda x: len(x) >= 8 and uppercase(x) and lowercase(x) and digit(x)
if valid_password(str1):
   print("Valid Password.")
else:
   print("Invalid Password.")


str1= "hello"
uppercase = lambda x: any(y.isupper() for y in x)
lowercase = lambda x: any(y.islower() for y in x)
digit = lambda x: any(y.isdigit() for y in x)
valid_password = lambda x: len(x) >= 8 and uppercase(x) and lowercase(x) and digit(x)
if valid_password(str1):
   print("Valid Password.")
else:
   print("Invalid Password.")




''' 7)
Write a Python program to sort a list of tuples using Lambda.


# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]


# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_scores = sorted(original_scores, key=lambda x: x[1])
print(sorted_scores)

