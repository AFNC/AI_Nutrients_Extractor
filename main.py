import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from transformers import DetrFeatureExtractor
from transformers import TableTransformerForObjectDetection
from ultralyticsplus import render_result
from ultralytics import YOLO
import paddleocr
from paddleocr import PaddleOCR, draw_ocr
from pymongo import MongoClient
import preprocessing
import classification
import detectionn
import structurerecognition
import textextraction
import dumptodatabase

def pipeline(image):
    
    model0 = tf.keras.models.load_model(
           ('resnetv2_10epochs.keras'),
           custom_objects={'KerasLayer':hub.KerasLayer}
    )
    
    #hub_layer = hub.KerasLayer(r'C:\Users\SCC\AppData\Local\Temp\tfhub_modules\145bb06ec3b59b08fb564ab752bd5aa222bfb50a')
    #model0 = keras.Sequential([hub_layer])
    
    model1 = YOLO('runs/detect/train5/weights/last.pt')
    model1.overrides['conf'] = 0.5  # NMS confidence threshold
    model1.overrides['iou'] = 0.45  # NMS IoU threshold
    model1.overrides['agnostic_nms'] = False  # NMS class-agnostic
    model1.overrides['max_det'] = 1  # maximum number of detections per image
    
    model3 = TableTransformerForObjectDetection.from_pretrained("microsoft/table-transformer-structure-recognition")
    model2 = PaddleOCR(use_angle_cls=False, lang='en')
    
    image0 = preprocessing.preprocess(image)
    print('Image has been preprocessed')
    label = classification.classify(image0, model0)
    print('Image has been classified', label)
    
    if label == 'Table':
        print('Nutrition Table has been recognized')
        detected_table = detectionn.detect_table(image, model1)
        print('Nutrition Table has been detected')
        detected_cols = structurerecognition.detect_cols(detected_table, image, model3)
        print('Nutrition Table columns have been detected')
        text = textextraction.image_to_text(detected_cols, model2)
        print('Nutrition information has been extracted')
        result = dumptodatabase.save_to_mongodb(text)
        print(result)
        return text
    return {'Nutrition Table does not exist':''}
        