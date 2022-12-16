import sys
def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A=[]
for _ in range(N):
    A.append(int(input()))

cnt=0
for coin in A[::-1]:
    cnt += K // coin
    K %= coin

print(cnt)