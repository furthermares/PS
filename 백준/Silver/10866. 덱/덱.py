import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

n = int(input())

q = deque()
for _ in range(n):
    m = input()

    if m[:10] == "push_front":
        q.appendleft(m[11:])
    elif m[:9] == "push_back":
        q.append(m[10:])
    elif m[:9] == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif m[:8] == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
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