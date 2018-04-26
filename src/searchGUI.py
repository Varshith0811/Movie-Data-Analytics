from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

from movie import *
from machineLearning import predictRating

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

movieInfo = OMDBApi(title, 'movie', year)
movieData = parseJSON(movieInfo)


searchFrame.grid_forget()
window.title(title + ' - ' + year)
resultsFrame = Frame()
resultsFrame.grid()
resultsFrame.tkraise()
movieData = ''
for k, v in movieInfo.items():
    if k == "Runtime":
        outputLength = v
    elif k == "Awards":
        outputNom = v
    elif k == "imdbVotes":
        outputRating = v
    elif k == "Genre":
        outputGenre = v.split(", ")
    elif k == "imdbRating":
        actualScore = v
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
    movieDataLabel = Label(resultsFrame, text = movieData)
    movieDataLabel.grid(sticky = W)

posterURL = getPoster(movieInfo)
response = requests.get(posterURL)
image = Image.open(BytesIO(response.content))
poster = ImageTk.PhotoImage(image)
posterLabel = Label(image=poster)
posterLabel.image = poster # keeps a reference to avoid Python garbage collection removing image while still being displayed by Tk
posterLabel.grid(row = 0, column = 3, padx = 20)

# window.update()
# print(window.winfo_width())
# print(movieDataLength)

# f=Frame(height = 3, width = window.winfo_width() - 1000, pady = 10, bg="black")
# f.grid(sticky = 'ew')

# actualRatingStr = "Actual Rating: " + str(actualScore)
# predictedRatingStr = "Predicted Rating: " + str(predictedRating)
# differenceStr = "Difference: " + str((predictedRating - actualScore))
# datasetSizeStr = "Dataset Size: " + str(dataSize)



#Need to prep data to be sent to machineLearning.py
#outputLength, outputNom, outputGenre, outputRating, actualScore

outputLength = float(outputLength.split(" ")[0])*60.0
outputNom = outputNom.split(" ")[0]
#formatting isn't nice for noms
actualScore = float(actualScore)
for i, g in enumerate(outputGenre):
    if g == "Sci-Fi":
        outputGenre[i] = "SciFi"
outputRating = float(outputRating.replace(",", ""))
predictedRating, dataSize = predictRating(outputNom, outputGenre, outputRating, outputLength)
print("Actual Rating: " + str(actualScore))
print("Predicted Rating: " + str(predictedRating))
print("Difference: " + str((predictedRating - actualScore)))
print("Dataset Size: " + str(dataSize))

predictions = LabelFrame(resultsFrame, text="Prediction", padx=5, pady=5)
predictions.grid(row = 26, padx = 5, pady = 20, sticky = W)
predictionLabel = Label(predictions, text = "Actual Rating: " + str(actualScore)).grid(sticky = 'w')
predictionLabel = Label(predictions, text = "Predicted Rating: " + str(predictedRating)).grid(sticky = 'w')
predictionLabel = Label(predictions, text = "Difference: " + str((predictedRating - actualScore))).grid(sticky = 'w')
predictionLabel = Label(predictions, text = "Dataset Size: " + str(dataSize)).grid(sticky = 'w')

window.mainloop()
