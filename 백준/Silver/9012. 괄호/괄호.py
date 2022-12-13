import sys
def input(): return sys.stdin.readline().rstrip()

from collections import deque

T = int(input())
for i in range(T):
    stack = deque()
    inputs = input()

    flag = True
    for j in range(len(inputs)):
        if inputs[j] == "(":
            stack.append(0)
        else:
            if len(stack) == 0:
                flag = False
                break
            stack.pop()

    if flag and len(stack) == 0:
        print("YES")
    else:
        print("NO")