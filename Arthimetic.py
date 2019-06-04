k,a,d=map(int,input().split())
n=a
for i in range(k-1):
  a=a+d
  k+=a
print(k)

