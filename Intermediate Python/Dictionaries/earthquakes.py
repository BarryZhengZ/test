'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.


NOTE: No hard-coding allowed except for keys for the dictionaries


1) print out the number of earthquakes


2) iterate through the dictionary and extract the location, magnitude,
  longitude and latitude of the location and put it in a new
  dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
  magnitude > 6. Print out the new dictionary.


3) using the eq_dict dictionary, print out the information as shown below (first three shown):


Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364




Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604




Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628


'''


# extract dictionary from json
import json


infile = open('eq_data.json','r')
earthquake_data = json.load(infile)


#1) print out the number of earthquakes
print ("The number of earthquakes is: ", len(earthquake_data["features"]))
print()
#2) iterate through the dictionary and extract the location, magnitude,
#   longitude and latitude of the location and put it in a new
#   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
#   magnitude > 6. Print out the new dictionary.
eq_dict = {}


for eq in range(len(earthquake_data["features"])):
  if earthquake_data["features"][eq]["properties"]["mag"] > 6:
      location = earthquake_data["features"][eq]["properties"]["place"]
      magnitude = earthquake_data['features'][eq]["properties"]["mag"]
      longitude = earthquake_data['features'][eq]["geometry"]["coordinates"][0]
      latitude = earthquake_data['features'][eq]["geometry"]["coordinates"][1]
      eq_dict[eq] = {"location":location, "magnitude":magnitude, "longitude":longitude, "latitude":latitude}
print(eq_dict)
print()
#3) using the eq_dict dictionary, print out the information as shown below
for eq in eq_dict:
   print("Location: ",eq_dict[eq]["location"])
   print("Magnitude: ",eq_dict[eq]["magnitude"])
   print("Longitude: ",eq_dict[eq]["longitude"])
   print("Latitude: ",eq_dict[eq]["latitude"])
   print()
   print()

