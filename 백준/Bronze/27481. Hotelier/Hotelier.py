X=[0]*10
input()
for n in input():
 if n=="L":
  for i in range(10):
   if not X[i]:X[i]=1;break
 elif n=="R":
  for i in range(10):
   if not X[9-i]:X[9-i]=1;break
 else:X[int(n)]=0
print(*X,sep="")