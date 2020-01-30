#file name creat

import cv2 as cv
import os

list = ['2', '5', '3']

TEST_PATH = r'C:\Users\내꺼\Git_WorkSpace\DN_Python_Rab\Prozect\FindCoordinates\textfile\\'
for i in list:
    
    file = open(TEST_PATH + i + '.txt', 'w')

    file.close()

