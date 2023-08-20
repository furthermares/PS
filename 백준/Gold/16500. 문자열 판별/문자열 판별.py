input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

S = ins()
A = [ins() for _ in range(inp())]

dp = [False] * (len(S)+1)
dp[0] = True

for i in range(len(S)):
    if dp[i]:
        for a in A:
            if S[i:].startswith(a):
                dp[i+len(a)] = True

print(int(dp[-1]))