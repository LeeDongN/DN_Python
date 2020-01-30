import cv2 as cv
import os




#file contents create
def generate_text(each_coordinates_list, fname, sep):
    file = open(r"C:\Users\내꺼\Git_WorkSpace\DN_Python_Rab\Prozect\FindCoordinates\textfile\fname.txt", 'w')
    vstr = ''
    
    for a in each_coordinates_list:
        vstr = vstr + str(a)+ sep
    vstr = vstr.rstrip(sep)
    
    file.writelines(vstr)
    file.close()


generate_text(each_coordinates_list, 'fname', sep = ' ')