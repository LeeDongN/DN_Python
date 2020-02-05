import glob
import time
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os


#원하는 경로 지정 변수
path_mask = r'C:\program1\image_mask\\'

tif_mask = glob.glob(path_mask + '/*.tif')
png_mask = glob.glob(path_mask + '/*.png')
bmp_mask = glob.glob(path_mask + '/*.bmp')

#원하는 저장 공간
SAVE_PATH_mask = 'C:\program1\image_mask_modified\\'


def mask_cutting(x, y, w, h, SAVE_PATH_mask, basename, TYPE):
    
    mask_gray = cv2.imread(path_mask + basename[:-4] + TYPE, cv2.IMREAD_GRAYSCALE)
        
    mask_trim = mask_gray[y:y+h, x:x+w]
    cv2.imwrite(SAVE_PATH_mask + basename + '_mask', mask_trim)
    print(basename_m)

    