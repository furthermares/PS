input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())
inl=lambda:list(map(int,input().split()))

N,K = inm()
WV = [[0,0]]+[inl() for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]

for n in range(1,N+1):
    for k in range(1,K+1):
        w, v = WV[n]
       
        if k < w:
            dp[n][k] = dp[n-1][k]
        else:
            dp[n][k] = max(v + dp[n-1][k - w], dp[n-1][k])

print(max(dp[-1]))
