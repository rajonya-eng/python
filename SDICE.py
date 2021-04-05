# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    dc=int(n/4)
    topdc=n%4
    if(topdc==0):
        dc-=1
        topdc+=4
    dc1=0
    m=0
    if(topdc<4 and dc>=1):
        m=4-topdc
        dc-=1 
        dc1=1
    top1={0:0, 1:48, 2:52, 3:56}
        
    bottom=44
    top={1:20, 2:36, 3:51, 4:60}
    y=0
    x=top.get(topdc)
    y=dc*bottom
    z=dc1*top1.get(m)
    v=x+y+z
    print(v)
    
    