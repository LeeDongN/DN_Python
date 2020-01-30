import cv2 as cv
import os
import time


path_image = 'C:\program1\image'
image_file_list = os.listdir(path_image)
coordinates_list = []

#저장하고 싶은 경로
SAVE_PATH = r'C:\Users\내꺼\Git_WorkSpace\DN_Python_Rab\Project\FindCoordinates\textfile\\'


def generate_text(SAVE_PATH, each_coordinates_list, sep):
    
    file = open(SAVE_PATH + 'DATA_2' + '.txt', 'w')
    
    for a in range(len(each_coordinates_list)): 
        
        vstr = ''
        vstr = vstr + str(each_coordinates_list[a])+ sep         
        vstr = vstr.rstrip(sep)
           
        file.write(vstr)
        file.write("\n")
        file.write("\n")
        a += 1
        
    file.close()
        
    
    

def find_coordinates(SAVE_PATH):
    #이미지에서 좌표를 찾는다
    for a in image_file_list:
        image_path = os.path.join('C:\program1\image',a)
        img_binary = cv.imread(image_path, 0)
        contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        basename = os.path.basename(image_path)
        
        for cnt in contours:
            x, y, w, h = cv.boundingRect(cnt)
            
        line = []
        
        line.append(basename)
        line.append(str(x))
        line.append(str(y + h))
        line.append(str(x + w))
        line.append(str(y))
                
        coordinates_list.append(line)   
      
    
    generate_text(SAVE_PATH, coordinates_list, '\n')
        
        
startTime = time.time()
find_coordinates(SAVE_PATH)
endTime = time.time()

print(round(endTime - startTime, 2))