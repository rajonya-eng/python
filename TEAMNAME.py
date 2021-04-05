#Сhef has assembled a football team! Now he needs to choose a name for his team. There are N words in English that Chef considers funny. These words are s1,s2,…,sN.

#Chef thinks that a good team name should consist of two words such that they are not funny, but if we swap the first letters in them, the resulting words are funny. Note that under the given constraints, this means that a word is a non-empty string containing only lowercase English letters.

#Can you tell Chef how many good team names there are?

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
    
