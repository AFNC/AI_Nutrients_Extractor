import os
import shutil
import cv2
import json
import torch
import numpy as np
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt
from transformers import DetrFeatureExtractor


def detect_cols(detected_table, filepath, model):    
    
    filename = filepath.split('\\')[-1].split('.')[0]
    dst_path = 'E:/PYTHON_PROJECTS/NOTEBOOKS/predicted_columns'
    dst_path0 = 'E:/PYTHON_PROJECTS/NOTEBOOKS/extracted_columns'
    
    image = detected_table
    feature_extractor = DetrFeatureExtractor()
    encoding = feature_extractor(image, return_tensors="pt")
    encoding.keys()

    with torch.no_grad():
        outputs = model(**encoding)

    # colors for visualization
    COLORS = [[0.000, 0.447, 0.741], [0.850, 0.325, 0.098], [0.929, 0.694, 0.125],
              [0.494, 0.184, 0.556], [0.466, 0.674, 0.188], [0.301, 0.745, 0.933]]

    cols = []

    def plot_results(pil_img, scores, labels, boxes):
        #pil_img = cv2.cvtColor(pil_img, cv2.COLOR_RGB2BGR)
        colors = COLORS * 100
        counter = 0
        for score, label, (xmin, ymin, xmax, ymax), c  in zip(scores.tolist(), labels.tolist(), boxes.tolist(), colors):

            #if (xmax-xmin) > 3*(ymax-ymin):
            if (xmax-xmin) < (ymax-ymin):
                #ax.add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=False, color=c, linewidth=3))
                cropped_col = pil_img[int(ymin):int(ymax), int(xmin):int(xmax)]

                # adding lines for padding:
                WHITE = [255,255,255]
                cropped_col = cv2.copyMakeBorder(cropped_col,10,10,10,10,cv2.BORDER_CONSTANT,value=WHITE)
                # lines for padding
                
                cv2.imwrite(filename+str(counter)+'.png', cropped_col)
                shutil.move(os.getcwd()+'\\'+filename+ str(counter)+'.png', dst_path0+'\\'+filename+str(counter)+'.png')

                cols.append(cropped_col)

                text = f'{model.config.id2label[label]}: {score:0.2f}'
                #ax.text(xmin, ymin, text, fontsize=15, bbox=dict(facecolor='yellow', alpha=0.5))
                cv2.rectangle(pil_img, (int(xmin), int(ymin)), (int(xmax),int(ymax)), (255,0,0), 3)
                cv2.putText(pil_img, text, (int(xmin), int(ymin)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 3)
            
            counter+=1
            
        cv2.imwrite(filename+'.png', pil_img)
        shutil.move(os.getcwd()+'\\'+filename+'.png', dst_path+'\\'+filename+'.png')

    target_sizes = [(image.shape[0],image.shape[1])]
    results = feature_extractor.post_process_object_detection(outputs, threshold=0.6, target_sizes=target_sizes)[0]
    plot_results(image, results['scores'], results['labels'], results['boxes'])
    
    return cols