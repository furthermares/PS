import sys
input = lambda: sys.stdin.readline().rstrip()

N, S = map(int,input().split())
A = list(map(int,input().split()))
l, r = 0, 0
s = A[0]
ans = sys.maxsize
 
while True:
    if s >= S:
        s -= A[l]
        ans = min(ans, r - l + 1)
        l += 1
    else:
        r += 1
        if r == N:
            break
        s += A[r]
 
print(0) if ans == sys.maxsize else print(ans)
