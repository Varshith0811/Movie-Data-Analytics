import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz
import pydot
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

features = pd.read_csv('../data/imdb.csv', error_bad_lines=False)

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

# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_features, train_labels)

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
print(np.mean(predictions))


# Pull out one tree from the forest
tree = rf.estimators_[5]

# Export the image to a dot file
export_graphviz(tree, out_file = '../data/tree.dot', feature_names = feature_list, rounded = True, precision = 1)

# Use dot file to create a graph
(graph, ) = pydot.graph_from_dot_file('../data/tree.dot')

# Write graph to a png file
graph.write_png('../data/tree.png')
