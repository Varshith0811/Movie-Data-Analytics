import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
'''
Predicting by:
imbdbRating
ratingCount
nrOfWins
nrOfNomiations
nrOfPhotos
nrOfNewsArticles
nrOfUserReviews
Genre
'''

'''For Testing:'''
#features = pd.read_csv('../data/temps.csv')

'''Actual:'''

features = pd.read_csv('../data/imdb.csv', error_bad_lines=False, engine='python')

#One-Hot Encoding
#features = pd.get_dummies(features, sparse=True)

# Labels are the values we want to predict
labels = np.array(features['imdbRating'])

# Remove the labels from the features
# axis 1 refers to the columns
features= features.drop('imdbRating', axis = 1)

# Saving feature names for later use
feature_list = list(features.columns)

# Convert to numpy array
features = np.array(features)

# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)