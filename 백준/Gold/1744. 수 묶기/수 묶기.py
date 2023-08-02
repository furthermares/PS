input=__import__('sys').stdin.readline
inp=lambda:int(input())

pos, neg = [], []
ans = 0
for _ in range(inp()):
    n = inp()

    if n > 1:
        pos.append(n)
    elif n <= 0:
        neg.append(n)
    else:
        ans += 1

pos.sort()
neg.sort(reverse=True)

for lst in (pos, neg):
    while len(lst) > 1:
        ans += lst.pop() * lst.pop()
    if lst:
        ans += lst.pop()

print(ans)