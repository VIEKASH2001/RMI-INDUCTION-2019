import numpy as np
import cv2
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
cap = cv2.VideoCapture('ball video.mov')
i=1
j=0
k=0
l=0
cX=0
cY=0
xi=0
yi=0
xf=0
yf=0
time=50
x=[]
y=[]

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if(ret==True):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_green = np.array([70,90,0])
        upper_green = np.array([90,255,255])
        greenmask = cv2.inRange(hsv, lower_green, upper_green)
        blurred = cv2.GaussianBlur(greenmask, (5, 5), 0)
        ret,thresh = cv2.threshold(blurred,127,255,0)
        kernel = np.ones((5,5),np.uint8)
        erosion = cv2.erode(thresh,kernel,iterations = 4)
        dilation = cv2.dilate(erosion,kernel,iterations = 4)
        
        # Image Moment is a particular weighted average of image pixel intensities,
        # with the help of which we can find some specific properties of an image
        M = cv2.moments(thresh)
        # calculate x,y coordinate of center
        if (M["m00"] != 0):
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            j+=1
        else:
            cX, cY = cX, cY
            if(k==1):
                l+=1

        if(j!=i and j!=0 and k==0):
            k+=1
            
        if(j!=0 and i==j):
            if(k==1):
                k+=1
                xf=cX
                yf=cY
            x.append(cX)
            y.append(cY)
            i+=1

        cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret,centroid = cv2.threshold(gray,254,255,0)
    
    if (cv2.waitKey(time) and ret==False):
        break

    if (k==1):
        xi=cX
        yi=cY
        
plt.plot(x, y)
plt.show() 
x_new=[]
v=(xf-xi)/l
for i in range(l):
    xi+=v
    x_new.append(int(xi))                                                                  
x_new =np.asarray(x_new) 
x =np.asarray(x)
y =np.asarray(y) 
f = interp1d(x, y, fill_value='extrapolate', kind='cubic')
y_new = f(x_new)

cap2=cv2.VideoCapture('ball video.mov')

while(cap.isOpened()):
    ret, frame = cap2.read()
    if(ret==True):
          for i in range(l):
              if(i==l-1):
                  break
              j=i+1
              cv2.line(frame,(x_new[i],int(y_new[i])),(x_new[j],int(y_new[j])),(0,255,0),2)
    cv2.imshow("trajectory",frame)
    if (cv2.waitKey(time) and ret==False):
        break

cap2.release()
cv2.destroyAllWindows()
   

