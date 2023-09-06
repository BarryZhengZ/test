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
        view_filtered_players_report()
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
def view_filtered_players_report():
    print('-' * 30, 'Filtered Players Report', '-' * 30)
    print()
    print()

    #Enter filter criteria 
    print('     Enter any Filter Criteria...')
    search_team_code = input('          Team Code:     ')
    search_position_code = input('          Position Code: ')
    search_last_name = input('          Last Name:     ')
    search_first_name = input('          First Name:    ')
    search_weight_min = input('          Weight (min):  ')
    search_weight_max = input('          Weight (max):  ')
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
    
    #Display user choices

    #Display Filtered Report
    #Print field names
    print('Emp ID Last Name         First Name     Team Code Pos Code Player No Age Weight Height Years College                 ')
    print('-' * 6, '-' * 17, '-' * 14, '-' * 9, '-' * 8, '-' * 9, '-' * 3, '-' * 6, '-' * 6, '-' * 5, '-' * 24)    

    #Populate the filtered players list
    filtered_players = []
    



main()
