#------------------------------------------------------------------------------
#Name: Zhang, Zheng & Wang, James
#MIS 3301 – Spring,2022 
#Purpose: Victorino Player Reporting System
#File: MIS3301-TeamProject.py
#------------------------------------------------------------------------------

#import modules
import csv
import os
import random
from operator import itemgetter

#constants
PLAYER_FILE = 'NFL-players.csv' 

#Parallel Lists - Teams  
TEAM_CODES = ['ATF',  'AZC',  'BFB',  'BLR',  'CAP',  'CHB',  'CLB',  'CNB',  'DLC',  'DTL',
              'DVB',  'GBP',  'HST',  'INC',  'JKJ',  'KCC',  'LAC',  'LAR',  'LVR',  'MMD',
              'MNV',  'NEP',  'NOS',  'NYG',  'NYJ',  'PHE',  'PTS',  'SFN',  'STS',  'TBB',  'TNT',  'WAS']
TEAM_NAMES = ['Atlanta Falcons', 'Arizona Cardinals', 'Buffalo Bills', 'Baltimore Ravens', 'Carolina Panthers',
              'Chicago Bears', 'Cleveland Browns', 'Cincinnati Bengals', 'Dallas Cowboys', 'Detroit Lions',
              'Denver Broncos', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars',
              'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Las Vegas Raiders', 'Miami Dolphins',
              'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets',
              'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers',
              'Tennessee Titans', 'Washington Football Team']

#Parallel Lists - Positions
POS_CODES = ['C', 'CB', 'DE', 'DT', 'FB', 'G', 'K', 'LB', 'LS', 'NT', 'OT', 'P', 'QB', 'RB', 'S', 'TE', 'WR']
POS_NAMES = ['Center', 'Cornerback', 'Defensive End', 'Defensive Tackle', 'Fullback', 'Guard', 'Kicker', 'Linebacker', 'Long Snapper', \
             'Nose Tackle', 'Offensive Tackle', 'Punter', 'Quarterback', 'Running back', 'Safety', 'Tight End', 'Wide Receiver']

#Main Function
def main():

    #Open player CSV for reading
    infile = open(PLAYER_FILE, 'r')
    reader = csv.reader(infile)

    #Create players list
    players = []
    
    #Skip header row
    next(reader)

    #Load the players list from CSV file
    for row in reader:
        temp = []
        temp.append(row[0])
        temp.append(row[1])
        temp.append(row[2])
        temp.append(row[3])
        temp.append(row[4])
        temp.append(row[5])
        temp.append(row[6])
        temp.append(int(row[7]))
        temp.append(int(row[8]))
        temp.append(row[9])
        temp.append(row[10])
        players.append(temp)
        
    #Close the file 
    infile.close()
    
    #Display banner
    print('*' * 55)
    print(' ' * 9, 'Victorino Player Reporting System')
    print('*' * 55)
    print()

    #Display menu choice 
#    while selection != 'X':
    print('1 - Team Roster Report-Release 2.0')
    print('2 - Team Weight Analysis Report-Release 2.0')
    print('3 - Filtered Players Report')
    print('X - Exit')
    print()
    selection = input('Choose one report: ').upper()
    print()
    if selection == '1':
        view_team_roster_report()
    elif selection == '2':
        view_team_weight_analysis_report()
    elif selection == '3':
        view_filtered_players_report(players)
    elif selection == 'X':
        print('Thank you for using Victorino Player Reporting System!')
        import sys
        sys.exit()
    else:
        print('Invalid choice, please choose again!')


#Fn1 Team Roster Report
def view_team_roster_report():
    print('This function will be completed in Release 2.0')


#Fn2 Team Weight Analysis Report
def view_team_weight_analysis_report():
    print('This function will be completed in Release 2.0')


#Fn3 Filtered Players Report
def view_filtered_players_report(players):
    print('-' * 30, 'Filtered Players Report', '-' * 30)
    print()
    print()
    criteria_counter = 0
    #Enter filter criteria 
    print('     Enter any Filter Criteria...')
    search_team_code = input('          Team Code:     ').upper()
    search_position_code = input('          Position Code: ').upper()
    search_last_name = input('          Last Name:     ').title()
    search_first_name = input('          First Name:    ').title()
    search_weight_min = input('          Weight (min):  ')
##    if search_weight_min != '':
##        search_weight_min = int(search_weight_min)       
    search_weight_max = input('          Weight (max):  ')
##    if search_weight_max != '':
##        search_weight_max = int(search_weight_max)
    print()
    
    #Enter sort options 
    print('     Sort Options: ')
    print(' ' * 9, '1) Name')
    print(' ' * 9, '2) Team & Position')
    print(' ' * 9, '3) Weight')
    print()
    sort_option = input('          Enter a sort option (or enter for none): ')
    print()
    print()
    

    #Populate the filtered players list
    filtered_players = []
    
    #Filter players list 
    for row in players:
        meet_criteria = True
        emp_id = row[0]
        last_name = row[1]
        first_name = row[2]
        team_code = row[3]
        position_code = row[4]
        player_num = row[5]
        age = row[6]
        weight = int(row[7])
        height = int(row[8])
        year_of_exp = row[9]
        college = row[10]
        found_last_name = last_name.startswith(search_last_name[0:len(search_last_name) + 1])
        found_first_name = first_name.startswith(search_first_name[0:len(search_first_name) + 1])
        if search_team_code != team_code:
            meet_criteria = False
        elif search_position_code != position_code and search_position_code != '':
            meet_criteria = False
        elif not found_last_name and search_last_name != '': 
            meet_criteria = False
        elif not found_first_name and search_first_name != '': 
            meet_criteria = False
        elif search_weight_min != '' and not (int(search_weight_min) <= weight):
            meet_criteria = False
        elif search_weight_max != '' and not (int(search_weight_max) >= weight):
            meet_criteria = False
        if meet_criteria:
            filtered_players.append(row)
            criteria_counter += 1


    #Display user choices

    print(' ' * 5, '>' * 50, 'FILTERED REPORT', '>' * 50)
    filt_team = ''
    filt_position_code = ''
    filt_last_name = ''
    filt_first_name = ''
    filt_weight_min = ''
    filt_weight_max = ''

    if search_team_code != '':
        filt_team = '> Team: ' + search_team_code + '  '
    if search_position_code != '':
        filt_position_code = '> Position Code: ' + search_position_code + '  '
    if search_last_name != '':
        filt_last_name = '> Last Name: ' + search_last_name + '  ' 
    if search_first_name != '':
        filt_first_name = '> First Name: ' + search_first_name + '  '
    if search_weight_min != '':
        filt_weight_min = '> Weight (min): ' + str(search_weight_min) + '  '
    if search_weight_max != '':
        filt_weight_max = '> Weight (max): ' + str(search_weight_max)+ '  '
        
    print(' '  * 16, '>>', ' Filters:', ' ' * 7, filt_team, filt_position_code, filt_last_name, filt_first_name, filt_weight_min, filt_weight_max, sep = '')

    sort_fields = ''

    if sort_option == '1':
        sort_fields = 'Name'
    elif sort_option == '2':
        sort_fields = 'Team & Position'    
    elif sort_option == '3':
        sort_fields = 'Weight'
   
    print(' '  * 16, '>>', ' Sort Fields:', ' ' * 3, sort_fields, sep = '')
    print()
    print(' '  * 16, '>>', ' Met Criteria:','  ', criteria_counter, ' player(s)', sep = '')
    print()
    print()
    print()
    

#Print field names
    print('Emp ID Last Name         First Name     Team Code Pos Code Player No Age Weight Height Years College                 ')
    print('-' * 6, '-' * 17, '-' * 14, '-' * 9, '-' * 8, '-' * 9, '-' * 3, '-' * 6, '-' * 6, '-' * 5, '-' * 24)

#sorted players

    if sort_fields == 'Name':
        filtered_players = sorted(filtered_players, key = itemgetter(1, 2))
    elif sort_fields == 'Team & Position':
        filtered_players = sorted(filtered_players, key = itemgetter(3, 4))     
    elif sort_fields == 'Weight':
        filtered_players = sorted(filtered_players, key = itemgetter(7))   


    for row in filtered_players:
        
        emp_id = row[0]
        last_name = row[1]
        first_name = row[2]
        team_code = row[3]
        position_code = row[4]
        player_num = row[5]
        age = row[6]
        weight = int(row[7])
        height = int(row[8])
        year_of_exp = row[9]
        college = row[10]

        
        print(emp_id + ' ', format(last_name, '<17'), format(first_name, '<14'), \
        format(team_code, '^9'), format(position_code, '^8'), format(player_num, '^9'), format(age, '^4'), format(weight, '^4'), format(height, '^8'),
        format(year_of_exp, '^4'), college)
              
        

    

main()
