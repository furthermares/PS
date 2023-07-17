input = __import__('sys').stdin.readline
inp = lambda: int(input())
inl = lambda: list(map(int,input().split()))

I = [inl() for _ in range(inp())]
I.sort(key=lambda x: (x[1], x[0]))

ans = 0
now = 0
for s, e in I:
    if s >= now:
        ans += 1
        now = e
print(ans)