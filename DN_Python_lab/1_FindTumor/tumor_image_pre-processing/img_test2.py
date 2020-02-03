import cv2 as cv
import glob
import time
#아직 전역변수로 바꾸지 않아 X_R_line과 Y_R_line 값이 저장되지 않는다.
#여러개의 사진을 넣었을 때도 잘 작동하는 거 확인함.


#원하는 경로 지정 변수
path_image = 'C:\program1\image_raw'

tif = glob.glob(path_image + '/*.tif')
png = glob.glob(path_image + '/*.png')
bmp = glob.glob(path_image + '/*.bmp')

#이미지에 대한 기준값 x, y의 fixed 값을 받아서 grayscare 값 얻어냄
def pixel_CutCriteria_detail(img_gray_pixel_CutCriteria, width, height, img_gray):
    
    y_fixed = img_gray_pixel_CutCriteria[0][0]
    x_fixed = img_gray_pixel_CutCriteria[0][1]
    y_R_line = []
    x_R_line = []
    
    
    for i_x in range(0, width):
        
        criteria_pixel_x = img_gray.item(y_fixed, i_x)
        
        y_line = []
        y_line.append(i_x)
        y_line.append(criteria_pixel_x)
        
        y_R_line.append(y_line)
    
    
    for i_y in range(0, height):
        
        criteria_pixel_y = img_gray.item(i_y, x_fixed)
        
        x_line = []
        x_line.append(i_y)
        x_line.append(criteria_pixel_y)
        
        x_R_line.append(x_line)


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
        
        pixel_CutCriteria_detail(img_gray_pixel_CutCriteria, width, height, img_gray)

start = time.time()

pixel_CutCtireia(bmp)
end = time.time()

print(round(end - start))
