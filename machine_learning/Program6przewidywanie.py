#NIE DZIAŁA
import  cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pickle


imagine_path = "c:/Users/pawko/OneDrive/Pulpit/python/machine_learning/dwa.png"
image = cv.imread(imagine_path)[:,:,0]
image = np.invert(np.array([image]))

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)


#single_image = np.expand_dims(image, axis=0)
prediction = model.predict(image)
print("Prediction: {}".format(np.argmax(prediction)))
plt.imshow(image[0])
plt.show()