import cv2
import numpy as np

def emptyfunction(X):
    pass

windowname="Tracbar window"
cv2.namedWindow(windowname)
cv2.createTrackbar('X',windowname,0,512,emptyfunction)
cv2.createTrackbar('Y',windowname,0,512,emptyfunction)
cv2.createTrackbar('THICKNESS',windowname,0,10,emptyfunction)

while True:
    image=np.zeros((512,512,3),np.uint8)
    X=cv2.getTrackbarPos('X',windowname)
    Y=cv2.getTrackbarPos('Y',windowname)
    THICKNESS=cv2.getTrackbarPos('THICKNESS',windowname)
    if(THICKNESS==0):#this is done to avoid the ereor that occurs when the thickness is inputted as 0 in the cv2.line function
        THICKNESS=1#giving 1 as the minimum thickness value
    img = cv2.line(image,(0,0),(X,Y),(255,0,0),THICKNESS)    
    cv2.imshow(windowname,img)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
