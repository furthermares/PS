import sys
input = sys.stdin.readline
inm = lambda: map(int,input().split())

MAX_SQ = 1000000
MAX_N = 1001
num_factors = [0] * (MAX_SQ+1)
ans = [0] * MAX_N

p = 1
while p * p <= MAX_SQ:
    for i in range(p * p, MAX_SQ+1, p):
        num_factors[i] += 1
    p += 1

for i in range(MAX_SQ + 1):
    if not ans[num_factors[i]]:
        ans[num_factors[i]] = i

input()
for n in inm():
    if n < MAX_N and ans[n]:
        print(ans[n])
    else:
        print("Too big")