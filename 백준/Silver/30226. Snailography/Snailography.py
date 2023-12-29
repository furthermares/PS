input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

N=inp()
S=ins()

M=[["#"]*N for _ in range(N)]

dx=(-1,0,1,0)
dy=(0,1,0,-1)

ori=0
cur_len=0
max_len=2

x=y=N//2

for i in range(len(S)):
    M[x][y]=S[i]

    x+=dx[ori%4]
    y+=dy[ori%4]
    
    cur_len+=1
    if(cur_len==max_len//2):
        max_len+=1
        ori+=1
        cur_len=0
        
print(*[M[i][j] for i in range(N) for j in range(N) if M[i][j]!="#"], sep="")
print()