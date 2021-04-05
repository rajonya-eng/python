#There are N frogs (numbered 1 through N) in a line. For each valid i, the i-th frog is initially at the position i, it has weight Wi, and whenever you hit its back, it jumps a distance Li to the right, i.e. its position increases by Li. The weights of the frogs are pairwise distinct.

#You can hit the back of each frog any number of times (possibly zero, not necessarily the same for all frogs) in any order. The frogs do not intefere with each other, so there can be any number of frogs at the same time at each position.

#Your task is to sort the frogs in the increasing order of weight using the smallest possible number of hits. In other words, after all the hits are performed, then for each pair of frogs (i,j) such that Wi<Wj, the position of the i-th frog should be strictly smaller than the position of the j-th frog. Find the smallest number of hits needed to achieve such a state.



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
