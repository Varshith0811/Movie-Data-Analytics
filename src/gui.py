from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from movie import *
from machineLearning import predictRating

def searchAndPredict():
    #Create GUI window, title, and search
    window = Tk()
    searchFrame = Frame()
    window.title("Predict")
    searchFrame.grid()

    #frame.bind(<Return>, )

    #Title Entry Box
    titleLabel = Label(searchFrame, text = 'Title:').grid(sticky = E)
    titleEntry = Entry(searchFrame)
    titleEntry.grid(row = 0, column = 1, padx = 5, pady= 5)

    #Year Entry box
    yearLabel = Label(searchFrame, text = 'Year:').grid(sticky = E)
    yearEntry = Entry(searchFrame)
    yearEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

    #Get data from entry fields
    waitVariable = IntVar()
    searchButton = Button(searchFrame, text = 'Search and Predict', command = lambda: waitVariable.set(1))
    searchButton.grid(column = 1, padx = 30, pady = 10)
    searchButton.wait_variable(waitVariable)
    title = titleEntry.get()
    year = yearEntry.get()

    #Movie Object
    movieInfo = OMDBApi(title, 'movie', year)
    movieData = parseJSON(movieInfo)

    #Switch to results
    searchFrame.grid_forget()
    window.title(title + ' - ' + year)
    resultsFrame = Frame()
    resultsFrame.grid()
    resultsFrame.tkraise()

    #Display Movie Data from IMDB
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

    #Display the poster for the movie
    posterURL = getPoster(movieInfo)
    response = requests.get(posterURL)
    image = Image.open(BytesIO(response.content))
    poster = ImageTk.PhotoImage(image)
    posterLabel = Label(image=poster)
    posterLabel.image = poster # keeps a reference to avoid Python garbage collection removing image while still being displayed by Tk
    posterLabel.grid(row = 0, column = 3, padx = 20)

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
    print("Percent Error: " + str(abs(((predictedRating - actualScore)/actualScore)*100)) + "%")

    #Display Predictions
    predictions = LabelFrame(resultsFrame, text="Prediction", padx=5, pady=5)
    predictions.grid(row = 26, padx = 5, pady = 20, sticky = W)
    predictionLabel = Label(predictions, text = "Actual Rating: " + str(actualScore)).grid(sticky = 'w')
    predictionLabel = Label(predictions, text = "Predicted Rating: " + str(predictedRating)).grid(sticky = 'w')
    predictionLabel = Label(predictions, text = "Difference: " + str((predictedRating - actualScore))).grid(sticky = 'w')
    predictionLabel = Label(predictions, text = "Dataset Size: " + str(dataSize)).grid(sticky = 'w')
    predictionLabel = Label(predictions, text = "Percent Error: " + str(round(abs(((predictedRating - actualScore)/actualScore)*100),4)) + "%").grid(sticky = 'w')

    #Run the application Again
    restartWaitVar = IntVar()
    restartButton = Button(resultsFrame, text = 'Predict Again', command = lambda: restartWaitVar.set(1))
    restartButton.grid(pady = 10)
    restartButton.wait_variable(restartWaitVar)
    restart(window)

    window.mainloop()

def restart(window):
    window.destroy()
    print('\n')
    searchAndPredict()
