I=lambda:[*map(int,input().split())]
N,M=I()
G=[I()for _ in[0]*N]
print(min(sum(G[i][j]*(abs(i-r)+abs(j-c))for i in range(N)for j in range(M))for r in range(N)for c in range(M)))