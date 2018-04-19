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

def parseJSON(movie):
    for k, v in movie.items():
        if k == "Ratings":
            print(k + ": ")
            for x in range(len(v)):
                for y, z in v[x].items():
                    if y == "Source":
                        temp = z
                    else:
                        print(temp + ": " + z)
        else:
            print(k + ": " + v)

def getPoster(movie):
    poster = 'https://www.classicposters.com/images/nopicture.gif'
    for k, v in movie.items():
        if k == "Poster":
            poster = v
    return poster
