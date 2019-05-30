g,h=map(int,input().split())
for k in range(g,h+1):
    if k>1:
        for s in range(2,k):
            if k%s==0:
                break
        else:
            print(k,end=" ")
            
