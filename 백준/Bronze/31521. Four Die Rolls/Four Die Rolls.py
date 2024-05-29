from itertools import* 
N,A,x=int(input()),[*map(int,input().split())],0
for l in permutations(range(1,7),4):
 for n in range(N):
  if A[n]!=l[n]:break
 else:x+=1
print(x,6**(4-N)-x)