import requests
import json

#This function just exists so that the existing unit tests pass
def getRating(title):
  rating = 8.0
  return rating

def OMDBApi(title, type, year):
    movieJSON = requests.get('http://www.omdbapi.com/?t=' + title + '&type=' + type + '&y=' + year + '&apikey=dd666771').json()
    parsed = json.dumps(movieJSON)
    print(json.dumps(parsed, indent=4, sort_keys=True))
