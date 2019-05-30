s,r=map(int,input().split())
a=str(s)
l=len(a)
#print(l)
for i in range(s,r):
    tema=i
    rem=0
    while(i!=0):
        dig=i%10
        rem=rem+dig**l
        i=i//10
    if(tema==rem):
        print(rem,end=" ")
