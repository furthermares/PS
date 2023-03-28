import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = input()
a = [int(input()) for _ in range(n)]

stack = []

for i in s :					
    if i.isalpha():
        stack.append(a[ord(i) - ord('A')])
    else:
        y, x = stack.pop(), stack.pop()

        if i == '+':
            stack.append(x+y)
        elif i == '-':
            stack.append(x-y)
        elif i == '*':
            stack.append(x*y)
        elif i == '/':
            stack.append(x/y)

print('%.2f' %stack[0])