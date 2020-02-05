import glob
import time
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os


def img_cutting(DATA_KIND, SAVE_PATH):
    global TYPE
    #원하는 mask를 잘라 이름을 붙이기 위함.
    if not DATA_KIND:
        
        if '.png' in DATA_KIND[0]:
            TYPE = '.png'
        
        elif 'bmp' in DATA_KIND[0]:
            TYPE = '.bmp'
        
        