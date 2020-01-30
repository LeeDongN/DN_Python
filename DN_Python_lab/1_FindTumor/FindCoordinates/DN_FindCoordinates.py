import cv2 as cv
import os
import time


path_image = 'C:\program1\image'
image_file_list = os.listdir(path_image)
list_len = len(image_file_list)
coordinates_list = []



def generate_text(each_coordinates_list, file_name_list, sep):
    TEST_PATH = r'C:\Users\내꺼\Git_WorkSpace\DN_Python_Rab\Project\FindCoordinates\textfile\\'
    a = 0
    
    for i in file_name_list:
        
        file = open(TEST_PATH + i + '.txt', 'w')
        
        vstr = ''
    
        vstr = vstr + str(each_coordinates_list[a])+ sep
                
        vstr = vstr.rstrip(sep)
            
        file.writelines(vstr)
        a += 1
        
        file.close()
        
    
    

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
      
    
    generate_text(coordinates_list, image_file_list, ' ')
        
        
startTime = time.time()
find_coordinates(image_file_list)
endTime = time.time()

print(round(endTime - startTime, 2))