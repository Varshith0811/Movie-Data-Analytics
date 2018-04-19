from tkinter import *

from Movie import OMDBApi

master = Tk()

titleLabel = Label(master, text = 'Title:').grid(sticky = E)
titleEntry = Entry(master)
titleEntry.grid(row = 0, column = 1, padx = 5, pady= 5)

yearLabel = Label(master, text = 'Year:').grid(sticky = E)
yearEntry = Entry(master)
yearEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

waitVariable = IntVar()

searchButton = Button(master, text = 'Search', command = lambda: waitVariable.set(1))
searchButton.grid()

searchButton.wait_variable(waitVariable)
title = titleEntry.get()
year = yearEntry.get()

OMDBApi(title, 'movie', year)

master.mainloop()
