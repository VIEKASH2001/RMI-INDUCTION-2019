import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#blank=np.zeros((512,512,3),np.uint8)
n=0
b=0
g=0
r=0
kernel = np.ones((5,5),np.uint8)
bxi=0
byi=0
bxf=0
byf=0
gxi=0
gyi=0
gxf=0
gyf=0
rxi=0
ryi=0
rxf=0
ryf=0
dim = (5, 5)
focal_length=540#focal_length = (pixel_width x  distance) / object_width(measured previously) in pixels unit
PC_ratio=36#pixels to centimetres ratio
#THE BELOW VARIABLES HAVE TO BE MODIFIED ACCORDING TO THE OBJECT USED
bobject_width=3#in cm
gobject_width=3#in cm
robject_width=3#in cm
#ALL THE VELOCITIES ARE IN Centimetres/second unit
#ALL THE DISTANCES ARE IN Centimetres

while(1):
    bz=0
    gz=0
    rz=0
    cmin=640
    cmax=0
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(hsv, (5, 5), 0)
    
    bxi=bxf
    byi=byf
    lower_blue = np.array([85,255,130])
    upper_blue = np.array([120,255,255])
    bluemask = cv2.inRange(blurred, lower_blue, upper_blue)
    berosion = cv2.erode(bluemask,kernel,iterations = 4)
    bdilation = cv2.dilate(berosion,kernel,iterations = 4)
    bcontours,_ = cv2.findContours(bdilation , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    if(bcontours!= []):
        length=len(bcontours[0])
        for i in range(length):
             if(bcontours[0][i][0][0]<cmin):
                 cmin=bcontours[0][i][0][0]
             if(bcontours[0][i][0][0]>cmax):
                 cmax=bcontours[0][i][0][0]
        pixel_width=cmax-cmin
        bz= int((bobject_width*focal_length)/pixel_width)
    bM = cv2.moments(bdilation)
    if (bM["m00"] != 0):
            bcX = int(bM["m10"] / bM["m00"])
            bcY = int(bM["m01"] / bM["m00"])
            
    else:
            bcX, bcY = 0,0
    bxf=bcX
    byf=bcY
    bvx=int(((bxf-bxi)/0.005) / PC_ratio)
    bvy=int(((byf-byi)/0.005) / PC_ratio)
    cv2.putText(bdilation,"VELOCITIES:",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(bdilation,"X:"+str(bvx),(200,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(bdilation,"Y:"+str(bvy),(350,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(bdilation,"Z DISTANCE:"+str(bz),(0,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    
    gxi=gxf
    gyi=gyf
    lower_green = np.array([90,105,40])
    upper_green = np.array([110,255,255])
    greenmask = cv2.inRange(blurred, lower_green, upper_green)
    gerosion = cv2.erode(greenmask,kernel,iterations = 3)
    gdilation = cv2.dilate(gerosion,kernel,iterations = 3)
    gcontours,_ = cv2.findContours(gdilation , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    if(gcontours!= []):
        length=len(gcontours[0])
        for i in range(length):
             if(gcontours[0][i][0][0]<cmin):
                 cmin=gcontours[0][i][0][0]
             if(gcontours[0][i][0][0]>cmax):
                 cmax=gcontours[0][i][0][0]
        pixel_width=cmax-cmin
        gz= int((gobject_width*focal_length)/pixel_width)
    gM = cv2.moments(gdilation)
    if (gM["m00"] != 0):
            gcX = int(gM["m10"] / gM["m00"])
            gcY = int(gM["m01"] / gM["m00"])
    
    else:
            gcX, gcY = 0,0
    gxf=gcX
    gyf=gcY
    gvx=int(((gxf-gxi)/0.005) / PC_ratio)
    gvy=int(((gyf-gyi)/0.005) / PC_ratio)
    cv2.putText(gdilation,"VELOCITIES:",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(gdilation,"X:"+str(gvx),(200,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(gdilation,"Y:"+str(gvy),(350,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(gdilation,"Z DISTANCE:"+str(gz),(0,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    
    rxi=rxf
    ryi=ryf
    lower_red = np.array([60,220,255])
    upper_red = np.array([180,255,255])
    redmask = cv2.inRange(blurred, lower_red, upper_red)
    rerosion = cv2.erode(redmask,kernel,iterations = 4)
    rdilation = cv2.dilate(rerosion,kernel,iterations = 4)
    rM = cv2.moments(rdilation)
    rcontours,_ = cv2.findContours(rdilation , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    if(rcontours!= []):
        length=len(rcontours[0])
        for i in range(length):
             if(rcontours[0][i][0][0]<cmin):
                 cmin=rcontours[0][i][0][0]
             if(rcontours[0][i][0][0]>cmax):
                 cmax=rcontours[0][i][0][0]
        pixel_width=cmax-cmin
        rz= int((robject_width*focal_length)/pixel_width)
    if (rM["m00"] != 0):
            rcX = int(rM["m10"] / rM["m00"])
            rcY = int(rM["m01"] / rM["m00"])
            
    else:
            rcX, rcY = 0,0
    rxf=rcX
    ryf=rcY
    rvx=int(((rxf-rxi)/0.005) / PC_ratio)
    rvy=int(((ryf-ryi)/0.005) / PC_ratio)
    cv2.putText(rdilation,"VELOCITIES:",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(rdilation,"X:"+str(rvx),(200,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(rdilation,"Y:"+str(rvy),(350,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.putText(rdilation,"Z DISTANCE:"+str(rz),(0,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))

    
    Rbluemask = cv2.resize(bdilation, dim, interpolation = cv2.INTER_AREA)
    Rgreenmask = cv2.resize(gdilation, dim, interpolation = cv2.INTER_AREA)
    Rredmask = cv2.resize(rdilation, dim, interpolation = cv2.INTER_AREA)
    
    Rbluemask=Rbluemask/10
    Rgreenmask=Rgreenmask/10
    Rredmask=Rredmask/10
    
    Ibluemask=Rbluemask.astype(int)
    Igreenmask=Rgreenmask.astype(int)
    Iredmask=Rredmask.astype(int)
    
    if(cv2.countNonZero(Ibluemask)!=0 and n==0):
            b=b+1
            n=1
            text="BLUE"+ str(b)
            print(text)
        
            
    elif(cv2.countNonZero(Igreenmask)!=0 and n==0):
            g=g+1
            n=1
            text="GREEN"+ str(g)
            print(text)
            

    elif(cv2.countNonZero(Iredmask)!=0 and n==0):
            r=r+1
            n=1
            text="RED"+ str(r)
            print(text)
        
            
    if(cv2.countNonZero(Ibluemask)==0 and cv2.countNonZero(Igreenmask)==0 and cv2.countNonZero(Iredmask)==0 ):
            n=0
            
            
    if(b==10):
        text= "BLUE is the winner!!!!!"
        print(text)
        break
    
    elif(g==10):
        text= "GREEN is the winner!!!!!"
        print(text)
        break
    
    elif(r==10):
        text= "RED is the winner!!!!!"
        print(text)
        break
    
    cv2.imshow('bluemask',bdilation) 
    cv2.imshow('greenmask',gdilation) 
    cv2.imshow('redmask',rdilation)      
    if cv2.waitKey(5) == 27:
        break

print("GAME OVER XD")    
cv2.destroyAllWindows()
cap.release()

        

##res = cv2.bitwise_and(frame,frame, mask= mask)
##    b,g,r=cv2.split(res)
##    if(cv2.countNonZero(b)==0 and cv2.countNonZero(g)!=0 and cv2.countNonZero(r)!=0 ):
##          print(i)
##          i+=1
## if(cv2.countNonZero(Ibluemask)==0 and cv2.countNonZero(Igreenmask)!=0 and cv2.countNonZero(Iredmask)!=0 ):
##            print(i)
