input = __import__('sys').stdin.readline
inp = lambda: int(input())
inl = lambda: list(map(int,input().split()))

N = inp()
DW = [inl() for _ in range(N)]

able = []
ans = 0

DW.sort()

for date in range(N,0,-1):
    while DW and DW[-1][0] >= date:
        able.append(DW.pop()[1])
    if able:
        able.sort()
        ans += able.pop()

print(ans)