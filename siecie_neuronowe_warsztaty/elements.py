import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

file = open("C:/Users/pawko/OneDrive/Pulpit/python/siecie_neuronowe_warsztaty/PubChemElements_all.csv")
lines = file.readlines()[1:]
file.close
dane = np.array([l.split(',')[1:] for l in lines], dtype=float)
dane = dane - np.mean(dane, 0)
dane = dane / np.std(dane, 0)
#print(dane)
X = dane[:,:5]
y = dane[:, 6]


r = 0.7
idx = np.arange(len(y))
np.random.shuffle(idx)


idx_t = idx[:20]
idx_v = idx[20:]

Xt = X[idx_t]
Xv = X[idx_v]

yt = y[idx_t]
yv = y[idx_v]

regr = MLPRegressor(hidden_layer_sizes=(10), random_state=2, max_iter=2000, learning_rate_init=.1, activation='logistic', solver='sgd',)
regr.fit(Xt, yt)
ytp = regr.predict(Xt)
yvp = regr.predict(Xv)

plt.plot(yt, ytp,  'bo')
plt.plot(yv, yvp, 'ro')
plt.show()