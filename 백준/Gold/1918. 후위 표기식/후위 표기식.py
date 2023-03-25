import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
stack = []
ans = ""

for i in s:
    if i.isalpha():
        ans += i
    elif i == '(':
        stack.append(i)
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(i) 
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
while stack:
    ans += stack.pop()

print(ans)