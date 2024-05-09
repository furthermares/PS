def valid(x, y, n):
    for i in range(9):
        if n in (A[x][i],A[i][y]):
            return False
            
    nx,ny=(x//3)*3,(y//3)*3
    for dx in range(3):
        for dy in range(3):
            if A[nx+dx][ny+dy]==n:
                return False
    return True


A=[[*map(int,[*input()])]for _ in range(9)]

zero=[(i,j) for i in range(9) for j in range(9) if A[i][j]==0]

def dfs(idx):
    if idx==len(zero):
        [print(*r,sep="") for r in A]
        exit(0)

    x, y = zero[idx]
    for i in range(1,10):
        if valid(x,y,i):
            A[x][y]=i
            dfs(idx+1)
            A[x][y]=0
dfs(0)