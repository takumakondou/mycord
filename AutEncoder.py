from tensorflow.keras.datasets import mnist
from sklearn.model_selection import train_test_split

from tensorflow import keras
from tensorflow.keras.layers import Dense,Activation,Dropout
import numpy as np
import matplotlib.pyplot as plt
import random

(x_train, _), (x_test, _) = mnist.load_data()

num=[1,2,3,4,5,6,7,8]

X_train,X_test=x_train/255.0,x_test/255.0
X_train=np.array(X_train)
X_test=np.array(X_test)
X_train=X_train.reshape(-1,784)
X_test=X_test.reshape(-1,784)

random.shuffle(X_train)
random.shuffle(X_test)

model=keras.Sequential()

model.add(Dense(200,activation='relu',input_shape=(784,)))
model.add(Dropout(0.25))
model.add(Dense(100,activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(50,activation='relu'))
model.add(Dense(5,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(100,activation='relu'))
model.add(Dense(784,activation='relu'))

model.compile(optimizer='rmsprop',loss='mse',metrics=['mae'])

model.fit(X_train,X_train,epochs=40,batch_size=32,verbose=True)

Y_pred=model.predict(X_test)

fig, ax = plt.subplots(2, 8, figsize=(28, 28))


for j in range(8):

    ax[0, j].imshow(X_test[num[j]].reshape(28,28), cmap='Greys')
    ax[1, j].imshow(Y_pred[num[j]].reshape(28,28), cmap='Greys')
plt.show()

model.save('model')