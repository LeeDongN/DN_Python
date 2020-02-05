import cv2 as cv
import numpy as np
import math
import glob
import time

#원하는 경로 지정 변수
path_image = 'C:\program1\image_raw'

tif = glob.glob(path_image + '/*.tif')
png = glob.glob(path_image + '/*.png')
bmp = glob.glob(path_image + '/*.bmp')


def pixel_CutCtireia(DATA_KIND):
    
    img_gray_pixel_CutCriteria = []
    
    #Color to Gray
    for a in DATA_KIND:
        img_color = cv.imread(a, cv.IMREAD_COLOR)
        img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
        
        #사진의 정중앙 픽셀의 값 저장
        height, width = img_gray.shape
        
        y = round(height/2)
        x = round(width/2)
        
        #pixel = img_gray.item(y,x)
        
        line = []
        line.append(y)
        line.append(x)
        #line.append(pixel)
        
        img_gray_pixel_CutCriteria.append(line)
        
        #함수 호출 여러번 하지 않게 바꿔야 함.
        pixel_CutCriteria_detail(img_gray_pixel_CutCriteria, width, height, img_gray)

start = time.time()
pixel_CutCtireia(png)
pixel_CutCtireia(bmp)
end = time.time()

print(round(end - start))
