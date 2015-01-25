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

# plot data of sepal length  and sepal width
for i in range(len(features[:,0])):
    if target[i] == 0:
        setosa_sepal_length.append(features[i][0])
        setosa_sepal_width.append(features[i][1])
        setosa_petal_length.append(features[i][2])
        setosa_petal_width.append(features[i][3])
    if target[i] == 1:
        versicolor_sepal_length.append(features[i][0])
        versicolor_sepal_width.append(features[i][1])
        versicolor_petal_length.append(features[i][2])
        versicolor_petal_width.append(features[i][3])
    if target[i] == 2:
        virginica_sepal_length.append(features[i][0])
        virginica_sepal_width.append(features[i][1])
        virginica_petal_length.append(features[i][2])
        virginica_petal_width.append(features[i][3])

# plot for sepal length / sepal width
plt.subplot(231)
plt.title('sepal length / sepal width')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.plot(setosa_sepal_length, setosa_sepal_width, "ro", label='setosa')
plt.plot(versicolor_sepal_length, versicolor_sepal_width, "go", label='versicolor')
plt.plot(virginica_sepal_length, virginica_sepal_width, "bo", label='virginica')
plt.legend()

# plot for sepal length / petal length
plt.subplot(232)
plt.title('sepal length / petal length')
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.plot(setosa_sepal_length, setosa_petal_length, "ro", label='setosa')
plt.plot(versicolor_sepal_length, versicolor_petal_length, "go", label='versicolor')
plt.plot(virginica_sepal_length, virginica_petal_length, "bo", label='virginica')
# plt.legend()

# plot for sepal length / petal width
plt.subplot(233)
plt.title('sepal length / petal width')
plt.xlabel('sepal length')
plt.ylabel('petal width')
plt.plot(setosa_sepal_length, setosa_petal_width, "ro", label='setosa')
plt.plot(versicolor_sepal_length, versicolor_petal_width, "go", label='versicolor')
plt.plot(virginica_sepal_length, virginica_petal_width, "bo", label='virginica')
# plt.legend()

# plot for sepal width / petal length
plt.subplot(234)
plt.title('sepal width / petal length')
plt.xlabel('sepal width')
plt.ylabel('petal length')
plt.plot(setosa_sepal_width, setosa_petal_length, "ro", label='setosa')
plt.plot(versicolor_sepal_width, versicolor_petal_length, "go", label='versicolor')
plt.plot(virginica_sepal_width, virginica_petal_length, "bo", label='virginica')
# plt.legend()

# plot for sepal width / petal width
plt.subplot(235)
plt.title('sepal width / petal width')
plt.xlabel('sepal width')
plt.ylabel('petal width')
plt.plot(setosa_sepal_width, setosa_petal_width, "ro", label='setosa')
plt.plot(versicolor_sepal_width, versicolor_petal_width, "go", label='versicolor')
plt.plot(virginica_sepal_width, virginica_petal_width, "bo", label='virginica')
# plt.legend()

# plot for petal length / petal width
plt.subplot(236)
plt.title('petal length / petal width')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.plot(setosa_petal_length, setosa_petal_width, "ro", label='setosa')
plt.plot(versicolor_petal_length, versicolor_petal_width, "go", label='versicolor')
plt.plot(virginica_petal_length, virginica_petal_width, "bo", label='virginica')
# plt.legend()

# Avoid conflict of title
# plt.tight_layout()

# show the data
plt.show()
