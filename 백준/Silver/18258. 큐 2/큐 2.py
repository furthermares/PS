import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

n = int(input())

q = deque()
for _ in range(n):
    m = input()

    if m[:4] == "push":
        q.append(m[5:])
    elif m == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif m == "size":
        print(len(q))
    elif m == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif m == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif m == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])