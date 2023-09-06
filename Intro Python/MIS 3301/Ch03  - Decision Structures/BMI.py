#------------------------------------------------------------
#Name: Zhang, Zheng
#MIS 3301 – Spring,2022 
#Purpose: Body Mass Index Analysis 
#File: Ch3-HW-BMI-Analysis.py
#------------------------------------------------------------


#Constants
OLDERA_MIN = 65
MIDDLEA_MIN = 64
ADULT_MIN = 44


#Input: 1st part 
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
age = int(input('Enter age: '))


#Data validation on age
if age < 13:
    print('You do not meet the minimum age requirement for BMI Analysis')
    import sys
    sys.exit()


#Input: 2nd part
height_total_in = int(input('Enter height (in.): '))
weight = float(input('Enter weight (lbs.): '))


#Convert height (in) to feet & inches
height_ft = int(height_total_in / 12)
height_inch = height_total_in % 12
final_height = str(height_ft) + "'" + str(height_inch) + '"'


#Determine age category
if age >= OLDERA_MIN:
    age_category = 'Older Adult'
elif age >= MIDDLEA_MIN:
    age_category = 'Middle Adult'
elif age >= ADULT_MIN:
    age_category = 'Adult'
else:
    age_category = 'Adolescent'


#Calculate BMI
bmi = weight * 703 / (height_total_in ** 2)
final_bmi = round(bmi,1)


#Determine BMI level
if final_bmi >= 25:
    bmi_level = 'Overweight'
else:
    if final_bmi >= 18.5:
        bmi_level = 'Optimal'
    else:
        bmi_level = 'Underweight'


#Determine Doctor
if age >= 18:
    doctor_type = 'internal medicine doctor'
else:
    doctor_type = 'pediatrician'


#Determine Message
if bmi_level == 'Optimal':
    msg = "   Congratulations, your BMI level is Optimal!\n\
   Return next year for your BMI Analysis."
else:
    msg = '     Due to your BMI level of ' + bmi_level + ', you\n\
     should visit an '+ doctor_type + '\n     for further evaluation.'

    
#Output
print()
print(' ' * 12, 'Victorino Nutrition Center')
print('-' * 19, 'BMI Analysis', '-' * 19)
print()
print(' ' * 3, format('Name:','8'), last_name, ', ', first_name,sep = '')
print(' ' * 2, format('Age:','7'), age)
print(' ' * 2, format('Height:','7'), final_height)
print(' ' * 2, format('Weight:','7'), weight)
print()
print(format('*' * 44, '^50'))
print('   >> Client type:', age_category)
print('   >> BMI: ', final_bmi, ' (', bmi_level, ')', sep = '')
print()
print(msg)
print(format('*' * 44, '^50'))
