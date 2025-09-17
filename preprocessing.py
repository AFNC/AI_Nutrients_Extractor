# preprocessing.py
# will take raw image from frontend
# will resize image
# will normalize image
# will return preprocessed image as output

import cv2
import numpy as np

def preprocess(image):
    image = cv2.imread(image)
    print(image.shape)
    image = cv2.resize(image,(224,224))
    image = image / 255
    image = np.array([image])
    
    print(image.shape)
    
    return image