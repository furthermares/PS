import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
idx = [0] * N
s = input()
stack = []

for i in range(N):
    if s[i] == '(':
        stack.append(i)
    else:
        if stack:
            idx[stack[-1]] = 1
            idx[i] = idx[stack[-1]]
            stack.pop()
            
cnt = 0
ans = 0
for i in idx:
    if i == 1:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)