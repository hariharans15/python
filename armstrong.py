s=int(input())
a=str(s)
l=len(a)
#print(l)
tema=s
rem=0
while(s!=0):
    dig=s%10
    rem=rem+dig**l
    s=s//10
if(tema==rem):
    print("yes")
else:
    print("no")
