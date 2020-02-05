import cv2 as cv
import numpy as np

img_gray_pixel = []

img_color = cv.imread(r"C:\program1\image_raw\39.bmp", cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

height, width = img_gray.shape
#img_gray_pixel1 = np.zeros((height, width), np.uint8)

for y in range(0, height):
    for x in range(0, width):
        pixel = img_gray.item(y,x)
        
        line = []
        line.append(y)
        line.append(x)
        line.append(pixel)
        
        img_gray_pixel.append(line)
        
print(img_gray_pixel)



file = open(r'C:\program1\test.txt', 'w')

for a in range(len(img_gray_pixel)):
    
    vstr = ''
    vstr = vstr + str(img_gray_pixel[a])        

                       
    file.write(vstr)
    file.write("\n")
file.close()
