import cv2
img = cv2.imread('00-puppy.jpg')
while True:
    
    cv2.imshow('Puppy', img)
    
    #If we waited atleast 1 ms AND ESC (ASCII is 27) key is pressed, then break
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()