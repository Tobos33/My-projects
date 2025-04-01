import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.svm import SVC


data = load_breast_cancer()


X = data.data
Y = data.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=30)


model = SVC(kernel='linear', C=3)
model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)
print("SVC = " + str(accuracy))


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
knn_accuracy = knn.score(X_test, Y_test)
print("knn = " + str(knn_accuracy))

