import sys
def input(): return sys.stdin.readline().rstrip()

cow=[None]*10
ans=0
for i in range(int(input())):
    m, n = list(map(int, input().split()))
    m-=1
    if cow[m]!=None and cow[m] != n:
        ans+=1
    cow[m] = n
    
print(ans)