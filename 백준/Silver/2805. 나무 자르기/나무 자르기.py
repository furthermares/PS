import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
S = list(map(int,input().split()))

start, end = 1, max(S)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in S:
        if x > mid:
            total += x - mid
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)