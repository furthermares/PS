import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
len_n = len(str(n)) - 1

ans=0
for i in range(len_n):
    ans += 9*(10**i)*(i+1)
ans += (int(n) - (10**len_n) +1) *(len_n+1)

print(ans)