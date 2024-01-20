from heapq import*
N,M=map(int,input().split())
A,a=sorted([*map(int,input().split())]),0
heapify(p:=[0]*M)
for i in A:x=p[0]+i;a+=x;heappushpop(p,x)
print(a)