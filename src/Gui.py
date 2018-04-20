from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

from Movie import *


window = Tk()
searchFrame = Frame()

window.title("Movie Search")
searchFrame.grid()

#frame.bind(<Return>, )

titleLabel = Label(searchFrame, text = 'Title:').grid(sticky = E)
titleEntry = Entry(searchFrame)
titleEntry.grid(row = 0, column = 1, padx = 5, pady= 5)

yearLabel = Label(searchFrame, text = 'Year:').grid(sticky = E)
yearEntry = Entry(searchFrame)
yearEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

waitVariable = IntVar()

searchButton = Button(searchFrame, text = 'Search', command = lambda: waitVariable.set(1))
searchButton.grid(column = 1, padx = 30)

searchButton.wait_variable(waitVariable)
title = titleEntry.get()
year = yearEntry.get()

movie = OMDBApi(title, 'movie', year)
movieData = parseJSON(movie)


searchFrame.grid_forget()
window.title(title + ' - ' + year)
resultsFrame = Frame()
resultsFrame.grid()
resultsFrame.tkraise()

movieData = ''
for k, v in movie.items():
    if k == "Ratings":
        #print(k + ": ")
        movieData = k + ":"
        for x in range(len(v)):
            for y, z in v[x].items():
                if y == "Source":
                    temp = z
                else:
                    #print(temp + ": " + z)
                    movieData += "   " + temp + ": " + z
    else:
        #print(k + ": " + v)
        movieData = k + ": " + v
    movieDataLabel = Label(resultsFrame, text = movieData).grid(sticky = W)

posterURL = getPoster(movie)
response = requests.get(posterURL)
image = Image.open(BytesIO(response.content))
poster = ImageTk.PhotoImage(image)
posterLabel = Label(image=poster)
posterLabel.image = poster # keeps a reference to avoid Python garbage collection removing image while still being displayed by Tk
posterLabel.grid(row = 0, column = 3, padx = 20)


window.mainloop()
