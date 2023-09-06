#------------------------------------------------------------
#Name: Zhang, Zheng
#MIS 3301 – Spring,2022 
#Purpose: Budget Tool
#File: Ch3-HW-Budget-Tool.py
#------------------------------------------------------------


#Generate header lines
print('*' * 60)
print(' ' * 8, 'Welcome to Victorino Financial Planners')
print('*' * 60)
print()
month = input('What month is this budget analysis for: ')
print()


#Process Income
print('-' * 14, 'INCOME DATA ENTRY', '-' * 14)
enter_again = 'y'
income_counter = 0
income_entry = 0
while enter_again == 'y':
    print()
    input('   Enter income name:   ')
    income = float(input('   Enter income amount: '))
    income_counter += income
    income_entry += 1
    print()
    enter_again = input('   >>> Do you have more income to enter (y/n)?').lower()
income_avg = format(income_counter / income_entry, ',.2f')


#Income summary
print()
print('   Income Summary')
print('  ', '-' * 25)
print('   Total income:  ', '$', income_counter, sep = '')
print('   Total entries:', income_entry)
print()


#Process Expenses
print('-' * 14, 'EXPENSES DATA ENTRY', '-' * 14)
print()
expense_counter = 0
num_expense = int(input('   Enter number of expenses: '))
for x in range (0, num_expense):
    print()
    input('   Enter expense name:   ')
    expense = float(input('   Enter expense amount: '))
    expense_counter += expense
expense_avg = expense_counter / num_expense


#Expense summary
print()
print('   Expenses Summary')
print('  ', '-' * 25)
print('   Total expenses:  ', '$', format(expense_counter,',.2f'), sep = '')
print('   Total entries:  ', num_expense)
print('\n\n')


#Calculate Net Income
net_income = income_counter - expense_counter 


#Net Income Status Determination
if net_income / income_counter >= 0.25:
    msg = 'Excellent! Net is >= 25% of income'
else:
    msg = 'Caution! Reduce your expenses'


#Generate Summary Table
income_counter = format(income_counter, ',.2f')
print('*' * 60)
print(format('Victorino Financial Planners', '^60'))
print(format('Personal Budget Tool', '^60'))
print(format('for ' + month, '^60'))
print('*' * 60)
print()
print(' ' * 10, 'Total', ' ' * 6, 'Avg/Entry')
print(format('Income', '<8'), format('$' + str(income_counter), '>10'), format('$' + str(income_avg), '>15'), sep = '')
print(format('Expenses', '<8'), format(expense_counter, '>10,.2f'), format(expense_avg, '>15,.2f'), sep = '')
print('-' * 35)
print(format('Net', '<8'), format(net_income, '>10,.2f'), '  (', msg, ')', sep = '')
