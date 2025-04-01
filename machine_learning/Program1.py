import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('C:/Users/pawko/OneDrive/Pulpit/python/machine_learning/mat.csv', sep= ';')
data = data[['sex', 'age',  'studytime','absences', 'G1', 'G2', 'G3']]
data['sex'] = data['sex'].map({'F': 0, 'M': 1})

prediction = 'G3'
X = np.array(data.drop([prediction],axis = 1))
Y = np.array(data[prediction])

#plt.plot(X,Y)
#plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

model = LinearRegression()
model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)
print(accuracy)


X_new = np.array([[1, 18, 3, 40, 15, 15]])
Y_new = model.predict(X_new)
print(Y_new)

plt.scatter(data['studytime'], data['G3'], label = 'studytime/G3')
plt.title("Correlation")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
#plt.show()

plt.scatter(data['G2'], data['G3'], label = 'G2/G3')
plt.title("Correlation")
plt.xlabel("Second Grade")
plt.ylabel("Final Grade")
plt.legend()
#plt.show()








