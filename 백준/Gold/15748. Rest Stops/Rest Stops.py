input = __import__('sys').stdin.readline
inm = lambda: map(int,input().split())
inl = lambda: list(map(int,input().split()))

L, N, RF, RB = inm()
XC = [inl() for _ in range(N)]

XC.sort(key=lambda x:-x[1])

l = ans = 0
for i in range(N):
    if XC[i][0] > l:
        ans += (RF-RB) * (XC[i][0] - l) * XC[i][1]
        l = XC[i][0]
print(ans)