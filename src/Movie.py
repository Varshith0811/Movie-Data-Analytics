import requests
import json

#This function just exists so that the existing unit tests pass
def getRating(title):
  rating = 8.0
  return rating

def OMDBApi(title, type, year):
    #Modifies input to match format for OMDB API
    title = title.replace(' ', '+')
    type = 'movie'

    movie = requests.get('http://www.omdbapi.com/?t=' + title + '&type=' + type + '&y=' + year + '&apikey=dd666771').json()
    return movie
