input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

M, H = inm()

ans = 0
for _ in range(inp()):
    Ci, Bi = inm()
    ans += max(M * Ci, H * Bi)

print(ans)
