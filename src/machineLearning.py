import pandas as pd
import numpy as np

'''For Testing:'''
#features = pd.read_csv('../data/temps.csv')

'''Actual:'''

features = pd.read_csv('../data/imdb.csv', error_bad_lines=False)

#One-Hot Encoding
features = pd.get_dummies(features)

# Labels are the values we want to predict
labels = np.array(features['actual'])

# Remove the labels from the features
# axis 1 refers to the columns
features= features.drop('actual', axis = 1)

# Saving feature names for later use
feature_list = list(features.columns)

# Convert to numpy array
features = np.array(features)
