I=lambda:[*map(int,input().split())]
N,D=I()
A=sorted([*I()])
for i in range(N):
 if A[i*2+1]-A[i*2]>D:exit(print("No"))
else:print("Yes")