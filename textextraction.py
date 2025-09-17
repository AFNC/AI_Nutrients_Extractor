import cv2
import paddleocr
from paddleocr import PaddleOCR, draw_ocr

def image_to_text(detected_cols, model):
    
    #resized_image = cv2.resize(table_image, (500,250))
    #result = model.ocr(resized_image,cls=True)
    '''result = model.ocr(detected_cols, cls=True)
    print('here is result')
    nutrition_dict = {}

    for i in range(len(result[0])):
        print(result[0][i][-1][0])
                
        if i-1>=0 and not any(char.isdigit() for char in result[0][i-1][-1][0]):
            nutrition_dict[result[0][i-1][-1][0]] = []
            
            if any(char.isdigit() for char in result[0][i][-1][0]):
                nutrition_dict[result[0][i-1][-1][0]].append(str(result[0][i][-1][0]).replace(',','.'))
                
                if i+1<len(result[0]) and any(char.isdigit() for char in result[0][i+1][-1][0]):
                    nutrition_dict[result[0][i-1][-1][0]].append(str(result[0][i+1][-1][0]).replace(',','.'))

    #info = json.dumps(nutrition_dict, indent=4)'''
    
    cols_copy = detected_cols.copy()
    #######################
    temp_listt = []
    #######################

    for item in cols_copy:
        result = model.ocr(item,cls=True)
        for j in range(len(result[0])):
            #print(result[0][j][-1][0])
            if len(temp_listt)==0:
                if 'bohyd' in result[0][j][-1][0]:
                    temp_listt.append(item)
                    cols_copy.remove(item)
                    break

    temp_listt.extend(cols_copy)         
    print(len(temp_listt))
    nutrition_dict = {}

    for i in range(len(temp_listt)):
        a = ''
        result = model.ocr(temp_listt[i],cls=True)
        print('OCR results are below: ')
        for j in range(len(result[0])):
            print(result[0][j][-1][0])
            if 'rgy' in result[0][j][-1][0]:
                a = result[0][j][-1][0].replace(result[0][j][-1][0], 'Energy')
            elif 'bohyd' in result[0][j][-1][0]:
                a = result[0][j][-1][0].replace(result[0][j][-1][0], 'Carbohydrates')
            elif 'otein' in result[0][j][-1][0]:
                a = result[0][j][-1][0].replace(result[0][j][-1][0], 'Proteins')
            elif 'ats' in result[0][j][-1][0] or ('at' in result[0][j][-1][0] and 'ate' not in result[0][j][-1][0]):
                a = result[0][j][-1][0].replace(result[0][j][-1][0], 'Fats')
            elif 'ibre' in result[0][j][-1][0] or 'ire' in result[0][j][-1][0]:
                a = result[0][j][-1][0].replace(result[0][j][-1][0], 'Fibre')
            elif 'tritional' in result[0][j][-1][0] or 'ritional' in result[0][j][-1][0]:
                a = result[0][j][-1][0].replace(result[0][j][-1][0], 'Nutritional')
            else:
                a = result[0][j][-1][0]
            if i==0:
                nutrition_dict[a] = []
            elif i>0 and i<len(temp_listt) and j<len(nutrition_dict.keys()):
                print('j',j)
                print(len(nutrition_dict.keys()))
                keys = list(nutrition_dict)
                nutrition_dict[keys[j]].append(str(result[0][j][-1][0]).replace(',','.'))

    
    return nutrition_dict