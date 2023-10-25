def f():return list(map(int,input().split(":")))
A,B=f(),f()
a=[B[0]-A[0]+24,B[1]-A[1]]
if a[1]<0:
 a[1]+=60
 a[0]-=1
print("%02d:%02d"%(a[0],a[1]))