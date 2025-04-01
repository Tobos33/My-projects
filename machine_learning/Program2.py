import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

data= load_breast_cancer()

#print(data.feature_names)
#print(data.target_names)
#print(data.data)

X = np.array(data.data)
Y = np.array(data.target)
#print(X)
#print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.1)
knn = KNeighborsClassifier(n_neighbors= 5)
knn.fit(X_train, Y_train)

accuracy = knn.score(X_test, Y_test)
print(accuracy)

#X_new = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2]])
#Y_new = knn.predict(X_new)
#print(Y_new)


clf1 = KNeighborsClassifier(n_neighbors=5)
clf2 = GaussianNB()
clf3 = LogisticRegression()
clf4 = DecisionTreeClassifier()
clf5 = RandomForestClassifier()


