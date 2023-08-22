input=__import__('sys').stdin.readline
inp=lambda:int(input())
inl=lambda:list(map(int,input().split()))

MAX_N = 100001

for _ in range(inp()):
    N = inp()
    S = [inl(),inl()]

    dp = [[0]*3 for _ in range(MAX_N)]
    
    for i in range(N):
        dp[i+1][0] = max(dp[i][0], dp[i][1], dp[i][2])
        dp[i+1][1] = max(dp[i][0], dp[i][2]) + S[0][i]
        dp[i+1][2] = max(dp[i][0], dp[i][1]) + S[1][i]

    print(max(dp[N][0],dp[N][1],dp[N][2]))