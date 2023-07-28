input = __import__('sys').stdin.readline
inp = lambda: int(input())
inl = lambda: list(map(int,input().split()))

N = inp()
E = inl()
V = inl()

ans = 0
mn = V[0]

for i in range(N-1):
    if V[i] < mn:
        mn = V[i]
    ans += mn * E[i]

print(ans)