import requests
import json


# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")




outfile = open('hn.json', 'w')


json.dump(r.json(), outfile, indent=4)


submissionIDsList = r.json()


url = 'https://hacker-news.firebaseio.com/v0/item/35457341.json'
r = requests.get(url)


outfile = open('hn2.json','w')




json.dump(r.json(),outfile,indent=4)


list_of_dict = []




# Explore the structure of the data.
for id in submissionIDsList[:21]:
   url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
   r = requests.get(url)
   response_dict = r.json()


   title = response_dict['title']
   link = f"Link: http://news.ycombinator.com/item?id={id}"
   try:
       comments = response_dict['descendants']
   except:
       comments = 0


   a_dict = {'title':title, 'link':link, 'comments':comments}
   list_of_dict.append(a_dict)


from operator import itemgetter


list_of_dict = sorted(list_of_dict, key=itemgetter('comments'), reverse = True)


for x in list_of_dict:
   print(f"Title: {x['title']}")
   print(f"Link: {x['link']}")
   print(f"Comments: {x['comments']}")

