# classification.py
# will take preprocessed image from preprocessing.py
# will apply renet model prediction
# will output image label as output

import numpy as np
import cv2
import os
import matplotlib.pylab as plt
import tensorflow as tf
import tensorflow_hub as hub

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

def classify(image, model):
    print('Now classifying----------------------')
    label = model.predict(image)
    print('LABEL HAS BEEN PREDICTED')
    label = np.argmax(label, axis=1)
    print('THE LABEL IS ')
    
    if 1 in label:
        print('YESSSSSSSSSSSSSSSSSS')
        return 'Table'
    
