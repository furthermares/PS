import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
ropes=[]
for i in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

res=[]
for i in range(N):
    res.append(ropes[i]*(i+1))
    
print(max(res))