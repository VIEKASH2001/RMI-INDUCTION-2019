
a=input("enter the array of characters: ")
p=2
f=0
c=0
while(1):
    q=p
    while(1):
       if(a[0:p]==a[q:q+p]):
           f+=1    
       q+=p
       if(q>=len(a)):
           break
    if(len(a)/p==(f+1)):
        print("the reccuring pattern is: ",a[0:p])
        c=1
        break
    f=0    
    p+=1
    if(p==9):
         break
if(c==0):
    print("no reccuring pattern found!!!!!")
