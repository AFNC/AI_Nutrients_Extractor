import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralyticsplus import render_result
from ultralytics import YOLO
import shutil
import json

def detect_table(image, model):
    
    filename = image.split('\\')[-1].split('.')[0]
    print('FILENAMEEEEEEEEEEEEEEEE',filename)
    dst_path = 'E:/PYTHON_PROJECTS/NOTEBOOKS/extracted_tables'
    results = model(image, save=True)
    cropped_table = 0

    for result in results:
        for box in result.boxes.xyxy:
            boxes = box.tolist()
            (x1,y1,x2,y2) = (int(boxes[0]), int(boxes[1]), int(boxes[2]), int(boxes[3]))
            img = cv2.imread(image)
            cropped_table = img[y1:y2, x1:x2]
            
            cv2.imwrite(filename+'.png', cropped_table)
            shutil.move(os.getcwd()+'\\'+filename+'.png', dst_path+'\\'+filename+'.png')
            
    return cropped_table