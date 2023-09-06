
#------------------------------------------------------------------------------
#Name: Zhang, Zheng
#MIS 3301 – Spring,2022 
#Purpose: List Processing
#File: MIS3301-Ch7-HW-Travel.py
#------------------------------------------------------------------------------


#Import Modules
import textwrap 

#Destinations LIST
DESTINATIONS = ['Empire State Building - New York, NY',
                'Everglades National Park - Florida, FL',
                'Fort Worth Stockyards - Fort Worth, TX',
                'Rocky Mountain National Park - Estes Park, CO',
                'Grand Canyon National Park - Arizona, AZ',
                'Pikes Peak - Colorado, CO',
                'River Walk - San Antonio, TX']


#Destination Details LIST
DEST_DETAILS = ["""The Empire State Building is a 102-story[c] Art Deco skyscraper in Midtown Manhattan in New York City. It was designed by Shreve, Lamb & Harmon and built from 1930 to 1931. Its name is derived from "Empire State", the nickname of the state of New York. The building has a roof height of 1,250 feet (380 m) and stands a total of 1,454 feet (443.2 m) tall, including its antenna. [source:wikipedia.org]""",
                       """Everglades National Park is an American national park that protects the southern twenty percent of the original Everglades in Florida. The park is the largest tropical wilderness in the United States, and the largest wilderness of any kind east of the Mississippi River. [source:wikipedia.org]'""",
                       """The Fort Worth Stockyards is a historic district that is located in Fort Worth, Texas, north of the central business district. A 98-acre (40 ha) portion encompassing much of the district was listed on the National Register of Historic Places as Fort Worth Stockyards Historic District in 1976.[1] It holds a former livestock market which operated under various owners from 1866. [source:wikipedia.org]""",
                       """Rocky Mountain National Park is an American national park located approximately 55 mi (89 km) northwest of Denver[5] in north-central Colorado, within the Front Range of the Rocky Mountains. The main features of the park include mountains, alpine lakes and a wide variety of wildlife within various climates and environments, from wooded forests to mountain tundra. [source:wikipedia.org]""",                
                       """Grand Canyon National Park, located in northwestern Arizona, is the 15th site in the United States to have been named a national park. The park's central feature is the Grand Canyon, a gorge of the Colorado River, which is often considered one of the Wonders of the World. [source:wikipedia.org]""",
                       """Pikes Peak is the highest summit of the southern Front Range of the Rocky Mountains, in North America. The ultra-prominent 14,115-foot (4,302.31 m) fourteener is located in Pike National Forest, 12 miles (19 km) west of downtown Colorado Springs, Colorado. [source:wikipedia.org]""",                           
                       """The San Antonio River Walk (also known as Paseo del Río or simply as The River Walk) is a city park and network of walkways along the banks of the San Antonio River, one story beneath the streets of San Antonio, Texas, United States. Lined by bars, shops, restaurants, nature, public artwork, and the five historic missions, the River Walk is an important part of the city's urban fabric and a tourist attraction in its own right. [source:wikipedia.org]"""]

                      
#States 2D LIST  
STATES = [['AL' , 'Alabama' , 'Montgomery' , 'Yellowhammer' , 'Camellia' , 22 , '12/14/1819'],
            ['AK' , 'Alaska' , 'Juneau' , 'Willow Ptarmigan' , 'Forget-me-not' , 49 , '01/03/1959'],
            ['AZ' , 'Arizona' , 'Phoenix' , 'Cactus Wren' , 'Saguaro Cactus Blossom' , 48 , '02/14/1912'],
            ['AR' , 'Arkansas' , 'Little Rock' , 'Mockingbird' , 'Apple Blossom' , 25 , '06/15/1836'],
            ['CA' , 'California' , 'Sacramento' , 'California Valley Quail' , 'Golden Poppy' , 31 , '09/09/1850'],
            ['CO' , 'Colorado' , 'Denver' , 'Lark Bunting' , 'Columbine' , 38 , '08/01/1876'],
            ['CT' , 'Connecticut' , 'Hartford' , 'American Robin' , 'Mountain Laurel' , 5 , '01/09/1788'],
            ['DE' , 'Delaware' , 'Dover' , 'Blue Hen Chicken' , 'Peach Blossom' , 1 , '12/07/1787'],
            ['FL' , 'Florida' , 'Tallahassee' , 'Mockingbird' , 'Orange Blossom' , 27 , '03/03/1845'],
            ['GA' , 'Georgia' , 'Atlanta' , 'Brown Thrasher' , 'Cherokee Rose' , 4 , '01/02/1788'],
            ['HI' , 'Hawaii' , 'Honolulu' , 'Nene (Hawaiian Goose)' , 'Hibiscus' , 50 , '08/21/1959'],
            ['ID' , 'Idaho' , 'Boise' , 'Mountain Bluebird' , 'Syringa' , 43 , '07/03/1890'],
            ['IL' , 'Illinois' , 'Springfield' , 'Cardinal' , 'Native violet' , 21 , '12/03/1818'],
            ['IN' , 'Indiana' , 'Indianapolis' , 'Cardinal' , 'Peony' , 19 , '12/11/1816'],
            ['IA' , 'Iowa' , 'Des Moines' , 'Eastern Goldfinch' , 'Wild Rose' , 29 , '12/28/1846'],
            ['KS' , 'Kansas' , 'Topeka' , 'Western Meadowlark' , 'Native Sunflower' , 34 , '01/29/1861'],
            ['KY' , 'Kentucky' , 'Frankfort' , 'Kentucky Cardinal' , 'Goldenrod' , 15 , '06/01/1792'],
            ['LA' , 'Louisiana' , 'Baton Rouge' , 'Pelican' , 'Magnolia' , 18 , '04/30/1812'],
            ['ME' , 'Maine' , 'Augusta' , 'Chickadee' , 'White Pine Cone and Tassel' , 23 , '03/15/1820'],
            ['MD' , 'Maryland' , 'Annapolis' , 'Baltimore Oriole' , 'Black-Eyed Susan' , 7 , '04/28/1788'],
            ['MA' , 'Massachusetts' , 'Boston' , 'Chickadee' , 'Mayflower' , 6 , '02/06/1788'],
            ['MI' , 'Michigan' , 'Lansing' , 'Robin' , 'Apple Blossom' , 26 , '01/26/1837'],
            ['MN' , 'Minnesota' , 'St. Paul' , 'Common Loon' , 'Pink and White Ladys Slipper' , 32 , '05/11/1858'],
            ['MS' , 'Mississippi' , 'Jackson' , 'Mockingbird' , 'Magnolia' , 20 , '12/10/1817'],
            ['MO' , 'Missouri' , 'Jefferson City' , 'Bluebird' , 'Hawthorn' , 24 , '08/10/1821'],
            ['MT' , 'Montana' , 'Helena' , 'Western Meadowlark' , 'Bitterroot' , 41 , '11/08/1889'],
            ['NE' , 'Nebraska' , 'Lincoln' , 'Western Meadowlark' , 'Goldenrod' , 37 , '03/01/1867'],
            ['NV' , 'Nevada' , 'Carson City' , 'Mountain Bluebird' , 'Sagebrush' , 36 , '10/31/1864'],
            ['NH' , 'New Hampshire' , 'Concord' , 'Purple Finch' , 'Purple Lilac' , 9 , '06/21/1788'],
            ['NJ' , 'New Jersey' , 'Trenton' , 'Eastern Goldfinch' , 'Purple Violet' , 3 , '12/18/1787'],
            ['NM' , 'New Mexico' , 'Santa Fe' , 'Roadrunner' , 'Yucca Flower' , 47 , '01/06/1912'],
            ['NY' , 'New York' , 'Albany' , 'Bluebird' , 'Rose' , 11 , '07/26/1788'],
            ['NC' , 'North Carolina' , 'Raleigh' , 'Cardinal' , 'Dogwood' , 12 , '11/21/1789'],
            ['ND' , 'North Dakota' , 'Bismarck' , 'Western Meadowlark' , 'Wild Prairie Rose' , 39 , '11/02/1889'],
            ['OH' , 'Ohio' , 'Columbus' , 'Cardinal' , 'Scarlet Carnation' , 17 , '03/01/1803'],
            ['OK' , 'Oklahoma' , 'Oklahoma City' , 'Scissor-Tailed Flycatcher' , 'Mistletoe' , 46 , '11/16/1907'],
            ['OR' , 'Oregon' , 'Salem' , 'Western Meadowlark' , 'Oregon Grape' , 33 , '02/14/1859'],
            ['PA' , 'Pennsylvania' , 'Harrisburg' , 'Ruffed Grouse' , 'Mountain Laurel' , 2 , '12/12/1787'],
            ['RI' , 'Rhode Island' , 'Providence' , 'Rhode Island Red' , 'Violet' , 13 , '05/29/1790'],
            ['SC' , 'South Carolina' , 'Columbia' , 'Carolina Wren' , 'Yellow Jessamine' , 8 , '05/23/1788'],
            ['SD' , 'South Dakota' , 'Pierre' , 'Ring-Necked Pheasant' , 'American Pasqueflower' , 40 , '11/02/1889'],
            ['TN' , 'Tennessee' , 'Nashville' , 'Mockingbird' , 'Iris' , 16 , '06/01/1796'],
            ['TX' , 'Texas' , 'Austin' , 'Mockingbird' , 'Bluebonnet' , 28 , '12/29/1845'],
            ['UT' , 'Utah' , 'Salt Lake City' , 'California Gull' , 'Sego Lily' , 45 , '01/04/1896'],
            ['VT' , 'Vermont' , 'Montpelier' , 'Hermit Thrush' , 'Red Clover' , 14 , '03/04/1791'],
            ['VA' , 'Virginia' , 'Richmond' , 'Cardinal' , 'Dogwood' , 10 , '06/25/1788'],
            ['WA' , 'Washington' , 'Olympia' , 'Willow Goldfinch' , 'Western Rhododendron' , 42 , '11/11/1889'],
            ['WV' , 'West Virginia' , 'Charleston' , 'Cardinal' , 'Big Rhododendron' , 35 , '06/20/1863'],
            ['WI' , 'Wisconsin' , 'Madison' , 'Robin' , 'Wood Violet' , 30 , '05/29/1848'],
            ['WY' , 'Wyoming' , 'Cheyenne' , 'Meadowlark' , 'Indian Paintbrush' , 44 , '07/10/1890']]

def main():
    #Initialize variables
    enter_number = 0
    state_views = [0] * len(STATES)
    while enter_number != 'X'.upper():


        #Display header
        print('*' * 60)
        print(' ' * 8, 'Victorino Travel Tours')
        print('*' * 60)
        print()
        
        
        #Display destinations menu
        print('List of Available Destinations')
        print('-' * 40)
        for i in range(1, len(DESTINATIONS) + 1):
            print(i, ': ', DESTINATIONS[i-1], sep= '')
        print('X: Press to exit')

        
        #Prompt user for destination number
        print()
        enter_number = input('Enter a destination #: ').upper()
        print()


        #Bonus (+5pt): Validate user input 
        menu_choice = ['1','2','3','4','5','6','7','X']
        while enter_number not in menu_choice:
            print('Invalid number choice, please choose again...')
            enter_number = input('Enter a destination #: ')
        

        #Exit application, if requested by user
        if enter_number == 'X':
            import sys
            print('Thank you for using this application!')
            sys.exit()
        enter_num_int = int(enter_number)

        
        #Display destinations details
        print('*' * 70)
        print('Destination:', DESTINATIONS[enter_num_int - 1])
        print()
        print(textwrap.fill(DEST_DETAILS[enter_num_int - 1], 70))
        print('*' * 70)

        
        #Display state details
        print()
        state_confirm = input('Would you like to know more about the state (y/n)? ').lower()
        print()
        st_code = DESTINATIONS[enter_num_int - 1][-2:]
        st_count = 0
        if state_confirm == 'y':
            print(' ', '-' * 20)
            while st_count < 50:
                if st_code == STATES[st_count][0]:
                    print('  State:     ', st_code)
                    print('  Capital:   ', STATES[st_count][2])
                    print('  Bird:      ', STATES[st_count][3])
                    print('  Flower:    ', STATES[st_count][4])
                    print('  Join Order:', STATES[st_count][5])
                    print('  Join Date: ', STATES[st_count][6])
                    print('  Views:     ', state_views[st_count])
                    state_views[st_count] += 1
                    print(' ', '-' * 20)
                    break
                st_count += 1


        #Pause processing - wait for user keypress (this must loop back to the top to re-display the header & menu)
        print()
        input('Press enter to continue...')
        print()
                  

main()
