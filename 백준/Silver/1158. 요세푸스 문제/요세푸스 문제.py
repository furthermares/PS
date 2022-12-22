import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1,n+1)])
res = []

while q:
    q.rotate(-k+1)
    res.append(str(q.popleft()))

ans = ", ".join(res)
print(f"<{ans}>")