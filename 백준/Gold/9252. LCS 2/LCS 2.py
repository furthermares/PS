input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

S = ins()
T = ins()

dp = [[""]*(len(T)+1) for _ in range(len(S)+1)]

for i in range(1,len(S)+1):
    for j in range(1,len(T)+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1] + S[i-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)

print(len(dp[-1][-1]))
print(dp[-1][-1])