import sys
def input(): return sys.stdin.readline().rstrip()

str = input()

from collections import deque
q = deque()

if len(str) % 2 == 1:
    print(0)
else:
    ans=0
    tmp=1
    for i in range(len(str)):
        if str[i] == "(":
            q.append("(")
            tmp *= 2
        elif str[i] == ")":
            if not q or q[-1] == "[":
                ans = 0
                break
            if str[i-1] == "(":
                ans += tmp
            q.pop()
            tmp //= 2
        elif str[i] == "[":
            q.append("[")
            tmp *= 3
        elif str[i] == "]":
            if not q or q[-1] == "(":
                ans = 0
                break
            if str[i-1] == "[":
                ans += tmp
            q.pop()
            tmp //= 3

    if q:
        print(0)
    else:
        print(ans)