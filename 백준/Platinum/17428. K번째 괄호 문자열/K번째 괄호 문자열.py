input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())

N,K = inm()
N //= 2
K += 1

catalan = [[0]*(N+2) for _ in range(N+2)]
catalan[1][0] = 1

for i in range(1, N+2):
    for j in range(i, N+2):
        catalan[i][j] = catalan[i][j-1] + catalan[i-1][j]

x = N
y = N+1
ans = ""
if K > catalan[x][y]:
    ans = "-1"
else:
    while y > 1:
        if K <= catalan[x][y]:
            ans += "("
            x -= 1
        else:
            ans += ")"
            K -= catalan[x][y]
            y -= 1
            
print(ans)