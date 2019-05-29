j,k=map(int,input().split())
l=[]
for b in range(j,k):
    if b%2!=0 and b!=1:
        l.append(b)
print(*l)
