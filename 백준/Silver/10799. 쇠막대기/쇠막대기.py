import sys
def input(): return sys.stdin.readline().rstrip()

str = input()

from collections import deque
q = deque()

ans=0
for i in range(len(str)):
        
    if str[i] == "(":
        q.append(0)
    else:
        if str[i-1] == "(":
            ans += len(q) - 1
        else:
            ans += 1
        q.pop()

print(ans)