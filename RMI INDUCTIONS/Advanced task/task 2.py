import cv2
import numpy as np
windowname='drawing'
image=np.ones((512,512,3),np.uint8)
image=255*image
img = np.copy(image)
cv2.namedWindow(windowname)

f1=0
f2=0
x1=-1
y1=-1
x2=-1
y2=-1

i=1

def point_1(event,x,y,flags,parameters):
     global f1,x1,y1
     if(event==cv2.EVENT_LBUTTONDOWN):
         x1=x
         y1=y
     if(x1!=-1 and y1!=-1):
         f1=1
def point_2(event,x,y,flags,parameters):
     global f2,x2,y2
     if(event==cv2.EVENT_LBUTTONUP):
         x2=x
         y2=y
     if(x2!=-1 and y2!=-1):    
         f2=1
    
while(True):
    cv2.imshow(windowname,img)
    print("enter the comand")
    key = cv2.waitKey(0)
    if(key != ord('C') and key != ord('L') and key != ord('R') and key != ord('S') and key != ord('E') and key!= 27):
         print("invalid command!!!!!.....Re-enter:")
         continue
    if(key == ord('C') or key == ord('L') or key == ord('R') ):     
         print("draw the shape by dragging the mouse")
         while(f1==0):
              cv2.setMouseCallback(windowname,point_1)
              cv2.waitKey(100)
                   
         while(f2==0):
              cv2.setMouseCallback(windowname,point_2)
              cv2.waitKey(100)
                 
     
    if(key == ord('C') or key == ord('L') or key == ord('R') ):
         if key == ord('C'):
              X=int(abs(x2+x1)/2)
              Y=int(abs(y2+y1)/2)
              a=abs(X-x1)
              b=abs(Y-y1)
              cv2.ellipse(img,(X,Y),(a,b),0,0,360,(255,0,0),3)
              
         elif key == ord('L'):
             cv2.line(img, (x1,y1), (x2,y2), (0, 255, 0), 3)
             
         elif key == ord('R'):
             cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), 3)
        
    if key == ord('S'):
        text="paint window_"+str(i)+".jpg"
        i+=1
        cv2.imwrite(text,img)
        print("image saved!!!!")

    if key == ord('E'):
        img = np.copy(image)
        print("screen cleared!!!")

    if key == 27:
        break

    #reseting all the variables to their initial value    
    f1=0
    f2=0
    x1=-1
    y1=-1
    x2=-1
    y2=-1
    

print("END OF PAINTING (:")    
cv2.destroyAllWindows()


             
  
