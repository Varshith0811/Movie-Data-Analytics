import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz
import pydot
import csv
def predictRating(inputNom, inputGenre, inputRating, inputLength):
    #Inputs from OMDB
    if not isinstance(inputNom, float):
        inputNom = -1
    if not isinstance(inputLength, float):
        inputLength = 5400 #90min
    if not isinstance(inputRating, float):
        inputRating = -1

    dataSize = 0
    genreCount = 0
    main = pd.read_csv('../data/imdb.csv', error_bad_lines=False, dtype='float')
    ofile  = open('../data/temp.csv', "w")
    writer = csv.writer(ofile, delimiter=',', lineterminator = '\n')
    writer.writerow(main.head())
    if inputNom != -1:
        for i, row in main.iterrows():
            genreCount = 0
            for g in inputGenre:
                if row[g] == 1:
                    genreCount = genreCount+1
            '''
            Within:
            Nominations: 15
            Ratings: +/- 25%
            Movie Duration: 30min
            Genre: At least 50% same genres
            '''
            if abs(row['nrOfNominations']-inputNom) <= 15 and abs(row['ratingCount']-inputRating) <= row['ratingCount']*.25 and abs(row['duration']-inputLength) >= 1800 and genreCount/len(inputGenre) >= 0.5:
                writer.writerow(row)
                dataSize = dataSize+1
    #For when Noms doesn't come in
    elif inputNom == -1:
        for i, row in main.iterrows():
            genreCount = 0
            for g in inputGenre:
                if row[g] == 1:
                    genreCount = genreCount+1
            '''
            Within:
            NO NOMS
            Ratings: +/- 25%
            Movie Duration: 30min
            Genre: At least 50% same genres
            '''
            if abs(row['ratingCount']-inputRating) <= row['ratingCount']*.25 and abs(row['duration']-inputLength) >= 1800 and genreCount/len(inputGenre) >= 0.5:
                writer.writerow(row)
                dataSize = dataSize+1
    #For when Rating numbers don't come in
    elif inputRating == -1:
        for i, row in main.iterrows():
            genreCount = 0
            for g in inputGenre:
                if row[g] == 1:
                    genreCount = genreCount+1
            '''
            Within:
            Noms: 15
            NO RATINGS
            Movie Duration: 30min
            Genre: At least 50% same genres
            '''
            if abs(row['nrOfNominations']-inputNom) <= 15 and abs(row['duration']-inputLength) >= 1800 and genreCount/len(inputGenre) >= 0.5:
                writer.writerow(row)
                dataSize = dataSize+1
    '''This is for when it returns 0 rows -> it'll default to only finding similar genre movies'''
    if dataSize == 0:
        for i, row in main.iterrows():
            genreCount = 0
            for g in inputGenre:
                if row[g] == 1:
                     genreCount = genreCount+1
            #Only with genres
            if genreCount/len(inputGenre) >= 0.5:
                writer.writerow(row)
                dataSize = dataSize+1

    ofile.close()

    features = pd.read_csv('../data/temp.csv', error_bad_lines=False)

    labels = np.array(features['imdbRating'])

    features= features.drop('imdbRating', axis = 1)

    feature_list = list(features.columns)

    features = np.array(features)

    #Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25)

    #1000 decision trees
    rf = RandomForestRegressor(n_estimators = 1000)
    #Train the model on training data
    rf.fit(train_features, train_labels)

    #Predict
    predictions = rf.predict(test_features)
    return (np.mean(predictions), dataSize)