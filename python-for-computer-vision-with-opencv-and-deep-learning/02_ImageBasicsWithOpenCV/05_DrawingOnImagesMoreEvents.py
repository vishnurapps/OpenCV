import cv2
import numpy as np


##################
####VARIABLES#####
##################

drawing = False
ix = -1
iy = -1

################
####FUNCTION####
################

def draw_rectangle(event, x, y, flag, params):
    
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy),(x, y), (255,0,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy),(x, y), (255,0,0), -1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)


############################
#SHOWING IMAGE USING OPENCV#
############################

img = np.zeros ((512, 512, 3), np.int8)  #int8 gives grey color

while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()

