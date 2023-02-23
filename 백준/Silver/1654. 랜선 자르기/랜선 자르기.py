import sys
def input(): return sys.stdin.readline().rstrip()

N, K = map(int,input().split())
S = [int(input()) for _ in range(N)]

start, end = 1, max(S)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in S:
        total += x // mid
    if total < K:
        end = mid - 1
    else:
        start = mid + 1

print(end)