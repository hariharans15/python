z,x=map(int,input().split())
l=[]
for g in range(z+1,x):
    if g%2==0 and g!=1:
        l.append(g)
print(*l)

