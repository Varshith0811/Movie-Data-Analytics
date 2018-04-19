from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

from Movie import *

master = Tk()

titleLabel = Label(master, text = 'Title:').grid(sticky = E)
titleEntry = Entry(master)
titleEntry.grid(row = 0, column = 1, padx = 5, pady= 5)

yearLabel = Label(master, text = 'Year:').grid(sticky = E)
yearEntry = Entry(master)
yearEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

waitVariable = IntVar()

searchButton = Button(master, text = 'Search', command = lambda: waitVariable.set(1))
searchButton.grid(column = 1, padx = 30)

searchButton.wait_variable(waitVariable)
title = titleEntry.get()
year = yearEntry.get()

movie = OMDBApi(title, 'movie', year)
movieData = parseJSON(movie)

posterURL = getPoster(movie)
response = requests.get(posterURL)
image = Image.open(BytesIO(response.content))
poster = ImageTk.PhotoImage(image)

posterLabel = Label(image=poster)
posterLabel.image = poster # keeps a reference to avoid Python garbage collection removing image while still being displayed by Tk
posterLabel.grid(row = 0, column = 3, padx = 20)

master.mainloop()
