from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Load data by load_iris function from sklearn
data = load_iris()

# extract data
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target] # replace all parametors to strings of target_names

# Initialize lists
setosa_sepal_length = []
setosa_sepal_width = []
setosa_petal_length = []
setosa_petal_width = []
versicolor_sepal_length = []
versicolor_sepal_width = []
versicolor_petal_length = []
versicolor_petal_width = []
virginica_sepal_length = []
virginica_sepal_width = []
virginica_petal_length = []
virginica_petal_width = []

# put data into each list
for i in range(len(features[:,0])):
    if target[i] == 0:
        setosa_sepal_length.append(features[i][0])
        setosa_sepal_width.append(features[i][1])
        setosa_petal_length.append(features[i][2])
        setosa_petal_width.append(features[i][3])
    elif target[i] == 1:
        versicolor_sepal_length.append(features[i][0])
        versicolor_sepal_width.append(features[i][1])
        versicolor_petal_length.append(features[i][2])
        versicolor_petal_width.append(features[i][3])
    elif target[i] == 2:
        virginica_sepal_length.append(features[i][0])
        virginica_sepal_width.append(features[i][1])
        virginica_petal_length.append(features[i][2])
        virginica_petal_width.append(features[i][3])

plength = features[:, 2]
is_setosa = (labels == 'setosa')    # create array true if labels is setosa

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print('Maximum of setosa: {0}. '.format(max_setosa))
print('Minimum of others: {0}. '.format(min_non_setosa))

def apply_model(example):
  if example[2] < 2: print 'Iris Setosa'
  else: print 'Iris Virginica or Iris Versicolor'
