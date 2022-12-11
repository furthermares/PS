import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
d=[0]*M
s=[0]*M
for i in range(M):
    d[i], s[i] = map(int,input().split())

dx = [None,[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for i in range(M):
    visited=[[False]*N for _ in range(N)]
    #1
    for cloud in clouds:
        cloud[0] += dx[d[i]][0]*s[i]
        cloud[0] %= N
        cloud[1] += dx[d[i]][1]*s[i]
        cloud[1] %= N
    #2
    #for cloud in clouds:
        A[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = True
    #3
    #4
    for cloud in clouds:
        water = 0

        a=cloud[0]
        b=cloud[1]

        if 0<=a-1<=N-1 and 0<=b-1<=N-1:
            if A[a-1][b-1]:
                water += 1
        if 0<=a+1<=N-1 and 0<=b-1<=N-1:
            if A[a+1][b-1]:
                water += 1
        if 0<=a+1<=N-1 and 0<=b+1<=N-1:
            if A[a+1][b+1]:
                water += 1
        if 0<=a-1<=N-1 and 0<=b+1<=N-1:
            if A[a-1][b+1]:
                water += 1
        A[a][b] += water
    #5
    clouds_n = []
    for j in range(N):
        for k in range(N):
            if not visited[j][k] and A[j][k] >= 2:
                clouds_n.append([j,k])
                A[j][k] -= 2
                
    clouds = clouds_n

ans=0
for i in range(N):
    for j in range(N):
        ans+=A[i][j]

print(ans)