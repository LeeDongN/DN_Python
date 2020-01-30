import cv2 as cv
import os

path_image = 'C:\program1\image'
image_file_list = os.listdir(path_image)
coordinates_list = []



def find_coordinates(image):
    #이미지에서 좌표를 찾는다
    for a in image_file_list:
        image_path = os.path.join('C:\program1\image',a)
        img_binary = cv.imread(image_path, 0)
        contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            x, y, w, h = cv.boundingRect(cnt)
        #[(x0, y0), (x1, y1)] 형태로 저장
        x0 = x
        x1 = x + w
        y0 = y + h
        y1 = y
        
        line = []
        for j in range(1):
            line.append(x0)
            line.append(y0)
            line.append(x1)
            line.append(y1)
                
        coordinates_list.append(line)
        
    print(coordinates_list)
        
        

find_coordinates(image_file_list)
