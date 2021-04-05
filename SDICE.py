#Chef has N 6-sided standard dice. Each die has dimensions 1×1×1. Since Chef is bored during the quarantine, he decides to stack dice for fun.

#First, Chef forms four vertical stacks of dice (not necessarily with the same height; empty stacks are allowed) on his table, which together make up a pile of dice with base area up to 2×2. Among all such structures, the total visible surface area of Chef's structure must be the smallest possible.

#Then, Chef calculates the number of pips on the visible faces of all dice in the structure. A face of a die is visible if it does not touch the table or another die.

#Now, he is wondering: among all possible arrangements of dice, what is the maximum possible total number of visible pips? Since he is busy cooking, he is asking you to solve this.



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
    
    
