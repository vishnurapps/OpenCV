import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#We have to use DVIX codec for windows and XVID codec for linux

writer = cv2.VideoWriter('mysupervideo.mp4', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (width,height))

while True:
    ret, frame = cap.read()
    
    #Saving Image
    writer.write(frame)
    #Gray scale capture
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #cv2.imshow('frame', gray)

    #Color capture
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()