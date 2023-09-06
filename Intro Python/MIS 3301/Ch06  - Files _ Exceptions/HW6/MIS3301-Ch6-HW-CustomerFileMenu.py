#------------------------------------------------------------------------------
#Name: Zhang, Zheng
#MIS 3301 – Spring,2022 
#Purpose: Customer File Menu
#File: MIS3301-Ch6-HW-CustomerFileMenu.py
#------------------------------------------------------------------------------


#Import Modules
import csv
import os


#Global Constants 
CUSTFILE = 'customers.csv'
BKUPFILE = 'customers-BKUP.csv'
TEMPFILE = 'customers-TEMP.csv'


#MAIN--------------------------------------------------------------------------------------
def main():
    menu_choice = '0'
    while menu_choice != '99':
        print('*' * 55)
        print(' ' * 12, 'Victorino Customer Data')
        print()
        print(' 1 - View customer list')
        print(' 2 - Lookup a customer')
        print(' 3 - Enter new customer')
        print(' 4 - Update a customer')
        print(' 5 - Delete a customer')
        print()
        print(' 7 - Copy customer data from BKUP (for testing only)')
        print('99 - Exit')
        print('*' * 55)
        print()
        menu_choice = input('Enter a menu choice: ')
        if menu_choice == '1':
            view_list()
        elif menu_choice == '2':
            lookup_cust()
        elif menu_choice == '3':
            enter_new_cust()
        elif menu_choice == '4':
            update_cust()
        elif menu_choice == '5':
            delete_cust()
        elif menu_choice == '7':
            copy_data()
        elif menu_choice == '99':
            pass
        else:
            print('Invalid choice, please choose again')
        print()


#FUNCTIONS----------------------------------------------------------------------



#Fn1---------------------
def view_list():
    cust_count = 0
    print('-' * 40)
    print()
    print(' ' * 7, '***', 'Customer List', '***')
    print() 
    infile = open(CUSTFILE, 'r')
    reader = csv.reader(infile)
    fields = next(reader)
    print('   ', fields[0], fields[1], fields[2])
    print('   ', '-' * 7, '-' * 10, '-' * 10) 
    for row in reader:
        Cust_ID = row[0]
        Last_name = row[1]
        First_name = row[2]

        print('   ', format(Cust_ID, '7'), format(Last_name, '10'), format(First_name, '10'))
        cust_count += 1 
    print()
    print('   ', '>>>', 'Total customers:', cust_count)
    print()
    infile.close()
    
    
#FN2---------------------
def lookup_cust():
    found = False 
    infile = open(CUSTFILE, 'r')
    reader = csv.reader(infile)
    print('-' * 40)
    print()
    print(' ' * 7, '***', 'Lookup Customer', '***')
    print()
    search_id = input('    Enter a customer ID: ')
    print()
    for row in reader:
        cust_id = row[0]
        last_name = row[1]
        first_name = row[2]
        if cust_id == search_id:
            found = True
            print('    Customer record found')
            print('   ', '-' * 30)
            print('    Customer ID:', cust_id)
            print('   ', format('Last Name:', '12'), last_name)
            print('   ', format('First Name:', '12'), first_name)
            print()
            break
    if not found:
        print('    Customer ID not found')
    infile.close()

#Fn3---------------------
def enter_new_cust():
    print('-' * 40)
    print()
    print(' ' * 7, '***', 'Enter New Customer', '***')
    print() 
    outfile = open(CUSTFILE, 'a', newline = '')
    writer = csv.writer(outfile, delimiter = ',')
    cont = 'y'
    while cont != 'n':
        cust_id = input('    Enter customer ID: ')
        last_name = input('    Enter last name:   ')
        first_name = input('    Enter first name:  ')
        new_row = [cust_id, last_name, first_name]
        writer.writerow(new_row)
        print()
        print('    STATUS: Customer', cust_id, 'saved!')
        print()
        cont = input('Do you want to continue (y/n)? ')
    outfile.close()
        

#Fn4---------------------
def update_cust():
    print('-' * 40)
    print()
    print(' ' * 7, '***', 'Update Customer', '***')
    print() 
    found = False
    infile = open(CUSTFILE, 'r')
    outfile = open(TEMPFILE, 'a', newline = '')
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter = ',')
    fieldnames = next(reader)
    writer.writerow(fieldnames)
    search_id = input('    Enter a customer ID: ')
    print()
    print('    Enter new values (or press enter to skip)')
    print('   ', '-' * 40)
    for row in reader:
        cust_id = row[0]
        last_name = row[1]
        first_name = row[2]
        if cust_id == search_id:
            found = True
            new_cust_id = input('      Enter new customer ID: ')
            new_last_name = input('      Enter new last name:   ')
            new_first_name = input('      Enter new first name:  ')
            if new_cust_id == '' and new_last_name == '':
                new_row = [cust_id, last_name, new_first_name]
            elif new_cust_id == '' and new_first_name == '':
                new_row = [cust_id, new_last_name, first_name]
            elif new_cust_id == '':
                new_row = [cust_id, new_last_name, new_first_name]
            else:
                new_row = [new_cust_id, new_last_name, new_first_name]
            writer.writerow(new_row)
        else:
            writer.writerow(row)
    if found:
        print('    Status: Customer', search_id, 'updated!')
    else:
        print('Customer ID not found')
    infile.close()
    outfile.close()
    os.remove(CUSTFILE)
    os.rename(TEMPFILE, CUSTFILE)
            

#Fn5---------------------
def delete_cust(): 
    found = False 
    infile = open(CUSTFILE, 'r')
    outfile = open(TEMPFILE, 'w', newline = '')
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter = ',')
    print('-' * 40)
    print()
    print(' ' * 7, '***', 'Delete Customer', '***')
    print()
    search_id = input('    Enter a customer ID: ')
    print()
    for row in reader:
        cust_id = row[0]
        last_name = row[1]
        first_name = row[2]
        if cust_id == search_id:
            found = True
            print('    Customer record found')
            print('   ', '-' * 30)
            print('      Customer ID:', cust_id)
            print('     ', format('Last Name:', '12'), last_name)
            print('     ', format('First Name:', '12'), first_name)
            print()
            delete_confirm = input('    Are you sure you want to delete (y/n)? ').lower()
            if delete_confirm == 'y':
                print()
                print('    STATUS: Customer', search_id, 'deleted!')
                pass #skip writting 
            else:
                writer.writerow(row)
        else:
            writer.writerow(row)
    if not found:
        print('    Customer ID not found')


    infile.close()
    outfile.close()
    os.remove(CUSTFILE)
    os.rename(TEMPFILE,CUSTFILE)


#Fn7---------------------
def copy_data():
    from shutil import copyfile
    copyfile(BKUPFILE, CUSTFILE)



main()
