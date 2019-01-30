import cv2 
import numpy as np

# Capture the frame
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()

# Get gray scale image of first frame and make a mask in HSV color
prvsImg = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

hsv_mask = np.zeros_like(frame1)
hsv_mask[:,:,1] = 255

while True:
    ret, frame2 = cap.read()
    nextImg = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    
    # Check out the markdown text above for a break down of these paramters, most of these are just suggested defaults
    flow = cv2.calcOpticalFlowFarneback(prvsImg,nextImg, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    
    # Color the channels based on the angle of travel
    # Pay close attention to your video, the path of the direction of flow will determine color!
    mag, ang = cv2.cartToPolar(flow[:,:,0], flow[:,:,1],angleInDegrees=True)
    hsv_mask[:,:,0] = ang/2
    hsv_mask[:,:,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    
    # Convert back to BGR to show with imshow from cv
    bgr = cv2.cvtColor(hsv_mask,cv2.COLOR_HSV2BGR)
    cv2.imshow('frame2',bgr)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    # Set the Previous image as the next iamge for the loop
    prvsImg = nextImg

    
cap.release()
cv2.destroyAllWindows()