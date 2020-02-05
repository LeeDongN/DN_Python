import cv2
from matplotlib import pyplot as plt
import numpy as np

test = cv2.imread(r'C:\program1\image_raw\5.bmp')
test_gray = cv2.imread(r'C:\program1\image_raw\5.bmp', cv2.IMREAD_GRAYSCALE)

blur = cv2.GaussianBlur(test_gray, ksize = (5, 5), sigmaX = 0)
ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

edged = cv2.Canny(blur, 10, 250)


contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0


contours_xy = np.array(contours)
contours_xy.shape


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
b = 'org_trim'

img_trim = test[y:y+h, x:x+w]
cv2.imwrite('C:\program1\image_raw\\' + b + '.png', img_trim)














