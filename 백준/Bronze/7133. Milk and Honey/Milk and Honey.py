input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

M, DM = inm()
H, DH = inm()

ans = 0
for _ in range(inp()):
    Ci, Bi = inm()
    
    C = sum([max(M - DM * ci, 0) for ci in range(Ci)])
    B = sum([max(H - DH * bi, 0) for bi in range(Bi)])
    
    ans += max(C, B)

print(ans)
