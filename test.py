import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from model import make_model, IMAGE_SIZE
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img


def load_image(file_path: str):

    img = load_img(file_path, target_size=IMAGE_SIZE)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    # this is a Numpy array with shape (1, 3, 150, 150)
    x = x.reshape((1,) + x.shape)

    return x


model = make_model()
model.load_weights('first_try.h5')

labels = [name for name in os.listdir('PokemonData') if os.path.isdir(
    os.path.join('PokemonData', name))]

file_path = input('Enter File path to predict> ')
while file_path != 'q':

    image = load_image(file_path)
    prediction = model.predict([image])
    label_index = np.argmax(prediction)
    label = labels[label_index]

    img = mpimg.imread(file_path)
    imgplot = plt.imshow(img)
    plt.suptitle(label, fontsize=20)
    plt.axis('off')
    plt.show()

    file_path = input('Enter File path to predict> ')
