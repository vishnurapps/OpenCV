import cv2

#Callback function
def draw_rect(event, x, y, flags, params):
    global pt1, pt2, topLeftClicked, bottomRightClicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Reset the rectangle
        if topLeftClicked == True and bottomRightClicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeftClicked = False
            bottomRightClicked = False
        
        if topLeftClicked == False:
            pt1 = (x,y)
            topLeftClicked = True
        elif bottomRightClicked == False:
            pt2 = (x,y)
            bottomRightClicked = True
            

#Global variable
pt1 = (0,0)
pt2 = (0,0)
topLeftClicked = False
bottomRightClicked = False

#Connect to callback
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rect)

while True:
    ret, frame = cap.read()
    #Drawing based on global variables
    if topLeftClicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0,0,255),thickness=-1)
    if topLeftClicked and bottomRightClicked:
        cv2.rectangle(frame, pt1, pt2, color=(0,0,255), thickness=1)
    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()