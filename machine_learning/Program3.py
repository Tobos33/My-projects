from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
import pandas as pd
import matplotlib.pyplot as plt


clf1 = KNeighborsClassifier(n_neighbors=5)
clf2 = GaussianNB()
clf3 = LogisticRegression()
clf4 = DecisionTreeClassifier()
clf5 = RandomForestClassifier()



data= load_breast_cancer()

X = np.array(data.data)
Y = np.array(data.target)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.1)

clf1.fit(X_train, Y_train)
clf2.fit(X_train, Y_train)
clf3.fit(X_train, Y_train)
clf4.fit(X_train, Y_train)
clf5.fit(X_train, Y_train)




score = [clf1.score(X_test, Y_test), clf2.score(X_test, Y_test), clf3.score(X_test, Y_test), clf4.score(X_test, Y_test), 
clf5.score(X_test, Y_test)]



data = pd.read_csv('C:/Users/pawko/OneDrive/Pulpit/python/machine_learning/mat.csv', sep= ';')
data = data[['sex', 'age',  'studytime','absences', 'G1', 'G2', 'G3']]
data['sex'] = data['sex'].map({'F': 0, 'M': 1})

prediction = 'G3'
X = np.array(data.drop([prediction],axis = 1))
Y = np.array(data[prediction])

#plt.plot(X,Y)
#plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)


clf1.fit(X_train, Y_train)
clf2.fit(X_train, Y_train)
clf3.fit(X_train, Y_train)
clf4.fit(X_train, Y_train)
clf5.fit(X_train, Y_train)



score = [clf1.score(X_test, Y_test), clf2.score(X_test, Y_test), clf3.score(X_test, Y_test), clf4.score(X_test, Y_test), 
clf5.score(X_test, Y_test)]
print(score)