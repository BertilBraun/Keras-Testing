import os
import numpy as np

from model import make_model, IMAGE_SIZE
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img


'PokemonData/Zapdos/00e5ca5e91ca4f44be3d3d2383f96779.jpg'
'PokemonData\Squirtle\00000000.png'

model = make_model()
model.load_weights('first_try.h5')

labels = [ name for name in os.listdir('PokemonData') if os.path.isdir(os.path.join('PokemonData', name)) ]

file_path = input('Enter File path to predict>')
while file_path != 'q':

    img = load_img(file_path, target_size=IMAGE_SIZE)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    print(labels[np.argmax(model.predict([x]))])

    file_path = input('Enter File path to predict>')