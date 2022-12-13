import sys
def input(): return sys.stdin.readline().rstrip()

from collections import deque

stack = deque()

N = int(input())
for i in range(N):
    inputs = input().split()
    
    if inputs[0] == "push":
        stack.append(inputs[1])
    elif inputs[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif inputs[0] == "size":
        print(len(stack))
    elif inputs[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif inputs[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)