# cook your dish here

for t in range(int(input())):
    n=int(input())
    l=input().split()
    x={}
    for i in l:
        p=i[1:]
        if p in x:
            x[p].append(i[0])
        else:
            x[p]=[i[0]]
    x1=list(x.keys())
    s=0
    for i in range (len(x)):
        for j in range(i+1,len(x)):
            temp=len(set(x[x1[i]]+x[x1[j]]))
            s+=(temp-len(x[x1[i]]))*(temp-len(x[x1[j]]))
    print(2*s)
    