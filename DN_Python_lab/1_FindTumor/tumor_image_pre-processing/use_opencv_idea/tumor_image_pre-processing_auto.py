import glob
import time
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

#원하는 경로 지정 변수
path_image = r'C:\program1\image_raw\\'

tif = glob.glob(path_image + '/*.tif')
png = glob.glob(path_image + '/*.png')
bmp = glob.glob(path_image + '/*.bmp')

SAVE_PATH = 'C:\program1\imgae_raw_modified\\'
def load_img(DATA_KIND, SAVE_PATH):
    

    for a in DATA_KIND:
        img_color = cv2.imread(a)
        img_gray = cv2.imread(a, cv2.IMREAD_GRAYSCALE)
        basename = os.path.basename(a)
        
        #이미지의 윤곽선을 딴다
        blur = cv2.GaussianBlur(img_gray, ksize = (5, 5), sigmaX = 0)
        ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

        edged = cv2.Canny(blur, 10, 250)


        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        total = 0


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
        cv2.imwrite(SAVE_PATH + basename, img_trim)
        print(basename)

start = time.time()
load_img(bmp, SAVE_PATH)
load_img(png, SAVE_PATH)    
end = time.time()

print(round(end - time, 2))       
        
        
        
        
        
        
        
        
        
        
        
        
        