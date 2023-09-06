import requests
import json


# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")


outfile = open('output.json','w')


response_dict = r.json()


json.dump(response_dict,outfile,indent=4)


list_of_repos = response_dict['items']


print(f"Number of repos:{len(list_of_repos)}")


first_repo = list_of_repos[0]


for key in first_repo:
   print(key)




#Print out
#Name of Repo
print(f"Name: {first_repo['name']}")
#Owner of Repo
print(f"Owner: {first_repo['owner']['login']}")
#Number of stars
print(f"Stars:{first_repo['stargazers_count']}")
#When it was created
print(f"Created: {first_repo['created_at']}")
#When it was last updated
print(f"Updated: {first_repo['updated_at']}")
#Description
print(f"Description: {first_repo['description']}")


from plotly.graph_objs import Bar
from plotly import offline


repos,stars = [],[]


for repo in list_of_repos[:10]:
   repos.append(repo['name'])
   stars.append(repo['stargazers_count'])


data = [{
   "type":"bar",
   "x":repos,
   "y":stars,
   "marker":{
       "color":"rgb(60,100,150)",
       "line":{"width":1.5, "color":"rgb(25,25,25)"},
   },
   "opacity":0.6,
}]


my_layout = {
   "title":"Most-Starred Python Projects on Github",
   "xaxis":{"title":"Repository"},
   "yaxis":{"title":"Stars"}
}


fig = {"data":data, "layout":my_layout}


offline.plot(fig, filename='python_repos.html')

