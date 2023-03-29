import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
stack = []
cnt = 0

for i in s:
    if i == '(':
        stack.append(i)
    else:
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            cnt += 1

print(cnt + len(stack))