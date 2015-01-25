from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Load data by load_iris function from sklearn
data = load_iris()

features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target] # replace all parametors to strings of target_names

# Initialize lists
setosa_x = []
setosa_y = []
versicolor_x = []
versicolor_y = []
virginica_x = []
virginica_y = []

# plot data of setosa
for i in range(len(features[:,0])):
    if target[i] == 0:
        setosa_x.append(features[i][0])
        setosa_y.append(features[i][1])
    if target[i] == 1:
        versicolor_x.append(features[i][0])
        versicolor_y.append(features[i][1])
    if target[i] == 2:
        virginica_x.append(features[i][0])
        virginica_y.append(features[i][1])

plt.plot(setosa_x, setosa_y, "ro", label='setosa')
plt.plot(versicolor_x, versicolor_y, "go", label='versicolor')
plt.plot(virginica_x, virginica_y, "bo", label='virginica')

plt.title('setosa / versicolor / virginica')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend()

# show the data
plt.show()
