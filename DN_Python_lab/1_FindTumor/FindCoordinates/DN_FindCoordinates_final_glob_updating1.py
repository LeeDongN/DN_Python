#속도 개선함 update 1

import cv2 as cv
import os
import time
import glob

#원하는 경로 지정 변수
path_image = 'C:\program1\image'
i = 0

#저장하고 싶은 경로
SAVE_PATH = r'C:\Users\내꺼\Git_WorkSpace\DN_Python_lab\Project\FindCoordinates\textfile\\'

#.tif, .png, .bmp
ALL_FILE = glob.glob(path_image + '/*.*')


def generate_text(SAVE_PATH, each_coordinates_list,  sep):
    
    DATA_basename = ['tif', 'png', 'bmp']
    
    global i
    file = open(SAVE_PATH + 'DATA_{}'.format(DATA_basename[i]) + '.txt', 'w')
        
    for a in range(len(each_coordinates_list)): 
            
        vstr = ''
        vstr = vstr + str(each_coordinates_list[a])+ sep         
        vstr = vstr.rstrip(sep)
           
        file.write(vstr)
        file.write("\n")
        file.write("\n")
        a += 1
        
    file.close()
       
    i += 1
           
    

def find_coordinates(FILES, SAVE_PATH):
    
    coordinates_list = []
    #이미지에서 좌표를 찾는다
    for a in FILES:
        
        img_binary = cv.imread(a, 0)
        contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        basename = os.path.basename(a)
        
        for cnt in contours:
            x, y, w, h = cv.boundingRect(cnt)
        #[(x0, y0), (x1, y1)] 형태로 저장

        line = []
        
        line.append(basename)
        line.append(str(x))
        line.append(str(y + h))
        line.append(str(x + w))
        line.append(str(y))
                  
        coordinates_list.append(line)   
     
    generate_text(SAVE_PATH, coordinates_list,  '\n')
        
        
startTime = time.time()
find_coordinates(ALL_FILE, SAVE_PATH)

endTime = time.time()

print(round(endTime - startTime, 2))