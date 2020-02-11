import glob
import time
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import os

#raw_image 원하는 경로 지정 변수
path_image = r'C:\program1\image_raw\\'

tif = glob.glob(path_image + '/*.tif')
png = glob.glob(path_image + '/*.png')
bmp = glob.glob(path_image + '/*.bmp')

#img 원하는 저장 공간
SAVE_PATH_img = 'C:\program1\imgae_raw_modified\\'


#mask 원하는 저장 공간
SAVE_PATH_mask = 'C:\program1\image_mask_modified\\'

#mask 원하는 경로 지정 변수
path_mask = r'C:\program1\image_mask\\'


def mask_cutting(x, y, w, h, SAVE_PATH_mask, basename, TYPE):
    
    #data유형에 따라 (_mask + TYPE)를 바꿔줘야 함. 
    mask_gray = cv.imread(path_mask + basename[:-4] + '_mask'  + TYPE, cv.IMREAD_GRAYSCALE)
        
    mask_trim = mask_gray[y:y+h, x:x+w]
    cv.imwrite(SAVE_PATH_mask + basename + '_mask' + TYPE, mask_trim)
    print(basename + '_mask' + TYPE)
        
        

def img_cutting(DATA_KIND, SAVE_PATH):
    global TYPE
    
    #원하는 mask를 잘라 이름을 붙이기 위함.
    #tif파일 일 경우 elif문의 TYPE를 '.tif'로 바꿀 
    if not DATA_KIND:
        
        DATA_KIND = "$"
        
    else:
        
        if '.png' in DATA_KIND[0]:
            TYPE = '.png'
        
        elif 'bmp' in DATA_KIND[0]:
            TYPE = '.bmp'

    for a in DATA_KIND:
        
        if a == "$":
            continue
        
        img_color = cv.imread(a)
        img_gray = cv.imread(a, cv.IMREAD_GRAYSCALE)
        basename = os.path.basename(a)
        
        #이미지의 윤곽선을 딴다
        blur = cv.GaussianBlur(img_gray, ksize = (5, 5), sigmaX = 0)
        ret, thresh1 = cv.threshold(blur, 127, 255, cv.THRESH_BINARY)

        edged = cv.Canny(blur, 10, 250)


        contours, _ = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        contours_xy = np.array(contours)
        contours_xy.shape

        #이미지의 x, y의 최대 최소 값을 구한
        x_min, x_min = 0, 0
        value = list()
        
        for i in range(len(contours_xy)):
            for j in range(len(contours_xy[i])):
                value.append(contours_xy[i][j][0][0])
                x_min = min(value)
                x_max = max(value)


        y_min, y_min = 0, 0
        value = list()
        
        for i in range(len(contours_xy)):
            for j in range(len(contours_xy[i])):
                value.append(contours_xy[i][j][0][1])
                y_min = min(value)
                y_max = max(value)


        x = x_min
        y = y_min
        w = x_max - x_min
        h = y_max - y_min
        
        img_trim = img_color[y:y+h, x:x+w]
        cv.imwrite(SAVE_PATH + basename, img_trim)
        print(basename)

        mask_cutting(x, y, w, h, SAVE_PATH_mask, basename, TYPE)





startTime = time.time()
img_cutting(bmp,SAVE_PATH_img)
img_cutting(png, SAVE_PATH_img)    
endTime = time.time()

print(round(endTime - startTime, 2))       
        
        