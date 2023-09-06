#------------------------------------------------------------------------------
#Name: Zhang, Zheng
#MIS 3301 – Spring,2022 
#Purpose: Property Tax
#File: Ch5-HW-PropertyTaxes.py
#------------------------------------------------------------------------------


#Import Modules
import random


#Global Constants
INDENT = '   '
AVG_HOME_VL_PER_SQFT = 130
ACRE_TO_SQFT = 43560
LD_VL_PER_ACRE = 100000.00
PROPERTY_TAXR = 0.02
PROPERTY_TAXR_H = 0.017
PROPERTY_TAXR_O = 0.016


#MAIN--------------------------------------------------------------------------------------
def main():
    #Display company & application header 
    display_company_banner()
    display_application_title('Welcome to the Residential Property Tax Estimation Tool!')

    
    #INPUT-----------------------------------------------------
    #Get user input
    address = input('Enter property address: ')
    bldg_sqft = int(input('Enter building size (sqft): '))
    ld_front = float(input('Enter land effective front (ft): '))
    ld_depth = float(input('Enter land effective depth (ft): '))
    exempt_code = input('Enter exemption code - (H)omestead, (O)ver 65, or (N)one: ')

    
    #PROCESS---------------------------------------------------
    exemption_name = get_exemption_name(exempt_code)
    bldg_value = calc_bldg_value(bldg_sqft)
    ld_sqft = calc_land_square_footage(ld_front, ld_depth)
    ld_acres = calc_land_acres(ld_sqft, ACRE_TO_SQFT)
    ld_value = calc_land_value(ld_acres)
    property_tax_w_exempt, property_tax = calc_property_taxes(bldg_value, ld_value, exempt_code)
    confirmation_no = gen_confirmation_no()

    
    #OUTPUT---------------------------------------------------

    #Display report title
    print()
    print(INDENT, '-' * 60, sep = '')
    print(format('Property Tax Estimate Report', '^70'))
    print(INDENT, '-' * 60, sep = '')
    print()
    print(INDENT, '>>> ', 'Report for property located at: ', address, sep = '')
    print()

    
    #Display report results
    print(INDENT, 'Building: ', format(bldg_sqft, ','), ' sqft', sep = '')
    print()
    print(INDENT, 'Land Info', sep = '')
    print(INDENT * 2, 'Front:', format(ld_front, '9,.2f'), INDENT, 'Depth: ', ld_depth, sep = '')
    print(INDENT * 2, 'Sqft:', format(ld_sqft, '10,.2f'), INDENT, 'Acres: ', format(ld_acres, '.4'), sep = '')
    print()
    print(INDENT, 'Building market value:', format(bldg_value, '16,.2f'), sep = '')
    print(INDENT, 'Land market value:', format(ld_value, '20,.2f'), sep = '')
    print(INDENT, 'Taxes w/Current Exemptions:', format(property_tax_w_exempt, '11,.2f'), ' (', exemption_name, ')', sep = '')
    print(INDENT, 'Taxes w/o Exemptions:', format(property_tax, '17,.2f'), sep = '')

    
    #Display report footer
    print(INDENT, '-' * 60, sep = '')
    print(INDENT, 'Estimate Confirmation No: ', confirmation_no, sep = '')
    print()

    
#FUNCTIONS--------------------------------------------------------------------------------------

#FN1: Company banner
def display_company_banner():
    print()
    print('*' * 70)
    print(format('Victorino County Tax Assessor','^70'))
    print('*' * 70)
    print()

    
#FN2: Application title
def display_application_title(app_title):
    print(format(app_title,'^70'))
    print()

    
#FN3: Exemption name
def get_exemption_name(exempt_code):
    if exempt_code == 'H':
        exemption_name = 'Homestead'
    elif exempt_code == 'O':
        exemption_name = 'Over 65'
    else:
        exemption_name = 'None'
    return exemption_name


#FN4: Building value
def calc_bldg_value(bldg_sqft):
    bldg_value = AVG_HOME_VL_PER_SQFT * bldg_sqft
    return bldg_value


#FN5: Land sqft
def calc_land_square_footage(front, depth):
    ld_sqft = front * depth
    return ld_sqft


#FN6: Land acres
def calc_land_acres(ld_sqft, ACRE_TO_SQFT):
    ld_acres = ld_sqft / ACRE_TO_SQFT
    return ld_acres


#FN7: Land value
def calc_land_value(ld_acres):
    ld_value = LD_VL_PER_ACRE * ld_acres
    return ld_value


#FN8: Property taxes
def calc_property_taxes(bldg_value, ld_value, exempt_code):
    if exempt_code == 'H':
        property_tax_w_exempt = (bldg_value + ld_value) * PROPERTY_TAXR_H
        property_tax = (bldg_value + ld_value) * PROPERTY_TAXR 
    elif exempt_code == 'O':
        property_tax_w_exempt = (bldg_value + ld_value) * PROPERTY_TAXR_O
        property_tax = (bldg_value + ld_value) * PROPERTY_TAXR
    else:
        property_tax = (bldg_value + ld_value) * PROPERTY_TAXR
        property_tax_w_exempt = property_tax
    return property_tax_w_exempt, property_tax   


#FN9: Confirmation number
def gen_confirmation_no():
    confirmation_no = random.randint(100000,999999)
    return confirmation_no


main()
