import requests
import json


url = "https://api.fbi.gov/wanted/v1/list"
r = requests.get(url)


outfile = open('FBIinfo.json','w')
json.dump(r.json(), outfile, indent=4)


info_list = r.json()


for number in info_list["items"]:
   if 'ViCAP Missing Persons' in number['subjects']:
       if number["age_max"] is not None and number["age_max"] < 25:
           print()
           print("Name: " + number["title"])
           print("FBI direct link: " + number["files"][0]["url"])
           print("Gender: " + number["sex"])
           print("Age: " + str(number["age_max"]))
           print("Eye color: " + number["eyes"])
           print("Hair color: " + number["hair"])
           print("Weight: " + str(number["weight_min"]))
           print()



