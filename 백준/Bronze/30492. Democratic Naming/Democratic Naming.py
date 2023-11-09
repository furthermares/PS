from collections import Counter
N,M=map(int,input().split())
S=[input() for _ in range(N)]
for i in range(M):print(Counter(sorted(S[x][i] for x in range(N))).most_common(1)[0][0],end="")