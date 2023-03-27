import sys
input = lambda: sys.stdin.readline().rstrip()

S = input()

l, r = 0, 0
sum = 0

for i in S:
    if i == '(':
        l += 1
        sum += 1
    if i == ')':
        r += 1
        sum -= 1
    if sum < 0:
        print(r)
        exit(0)
    if sum == 0:
        l = 0
print(l)