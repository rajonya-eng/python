# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    w=[int(x) for x in input().split()]
    l=[int(x) for x in input().split()]
    s=sorted(w)
    pos=[]
    cnt=0
    for j in range(n):
        pos.append(j)
    for j in range(1,n):
        index=w.index(s[j])
        p=pos[w.index(s[j-1])]
        c=index
        
        while(c<=p):
            c+=l[index]
            pos[index]=c 
            cnt+=1
    print(cnt)