import os
import keras
from keras.layers import Dense, Activation, Dropout
from keras import datasets

import numpy as np

model_path = 'mnist.model'

mnist = datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# building the input vector from the 28x28 pixels
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# normalizing the data to help with the training
x_train /= 255
x_test /= 255

# TODO fix this
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

if not os.path.exists(model_path):

    model = keras.Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(10))
    model.add(Activation('softmax'))

    model.compile(loss="categorical_crossentropy",
                  optimizer="adam", metrics=["accuracy"])

    model.fit(x_train, y_train, batch_size=128,
              epochs=10, validation_split=0.1)

    score = model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])

    model.save(model_path)


mnist_model = keras.models.load_model(model_path)
predicted_classes = mnist_model.predict(x_test)

for p, y in zip(predicted_classes, y_train):
    print(np.argmax(p), np.argmax(y))
