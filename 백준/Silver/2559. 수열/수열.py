import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int,input().split())
A = [0] + list(map(int,input().split()))
S = [0] * (N+1)

for i in range(1, N+1):
    S[i] = S[i-1] + A[i]

ans = []
for r in range(K,N+1):
    ans.append(S[r]-S[r-K])

print(max(ans))