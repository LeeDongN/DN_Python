import cv2 as cv
import numpy as np
import math
import glob
import time


#return값 = y_R_line, x_R_line

x_gap = []
y_gap = []


#뒤 픽셀과 앞 픽셀의 차를 구해 그 차가 15 이상이면 x_gap에 저장한다. 또한 그 때의 픽셀 넘버를 저장한다. 
for i_Xgap in range(0, len(y_R_line)):
    
    a_Xgap = y_R_line[i_Xgap][1] - y_R_line[i_Xgap - 1][1]
    
    if a_Xgap >= 15:
        x_gap.append(i_Xgap)
        x_gap.append(a_Xgap)

print(x_gap)