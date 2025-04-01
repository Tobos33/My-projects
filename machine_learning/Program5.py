from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt


digits = load_digits()
data = scale(digits.data)

print(data[0])
plt.scatter(data[0],data[1])
plt.show()


clf = KMeans(n_clusters= 10, init= 'random', n_init=10)
clf.fit(data)

#clf.predict([...])
#Przewidywanie, do którego miejsca należy nowa data