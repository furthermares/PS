input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())

N,L,I = inm()

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0] = [1]*(N+1)

for i in range(1,N+1):
    dp[i][0] = dp[i-1][0]
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

for n in range(N, 0, -1):
    if I <= dp[n-1][L]:
        print('0', end="")
    else:
        print('1', end="")
        I -= dp[n-1][L]
        L -= 1