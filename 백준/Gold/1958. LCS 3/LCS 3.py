input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

S = ins()
T = ins()
U = ins()

dp = [[[0]*(len(U)+1) for _ in range(len(T)+1)] for _ in range(len(S)+1)]

for s in range(1,len(S)+1):
    for t in range(1,len(T)+1):
        for u in range(1,len(U)+1):
            if S[s-1] == T[t-1] == U[u-1]:
                dp[s][t][u] = dp[s-1][t-1][u-1] + 1
            else:
                dp[s][t][u] = max(dp[s-1][t][u], dp[s][t-1][u], dp[s][t][u-1])
    
print(dp[-1][-1][-1])