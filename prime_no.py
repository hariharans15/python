count=0
p=int(input())
if p>1:
    for i in range(2,p//2):
        if p%i==0:
            count+=1
            break
if count==1:
    print("no")
else:
    print("yes")
        
