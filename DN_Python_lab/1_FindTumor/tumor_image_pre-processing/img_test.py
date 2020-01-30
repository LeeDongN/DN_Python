import cv2 as cv

img_test_color = cv.imread(r"C:\program1\image_raw\01-0001.png", cv.IMREAD_COLOR)
img_test_gray = cv.cvtColor(img_test_color, cv.COLOR_BGR2GRAY)
resize_img = cv.resize(img_test_gray,(1000, 1000))
resize_img2 = cv.resize(img_test_color, (500,500))



cv.imshow("Show2", resize_img2)
cv.waitKey(0)
