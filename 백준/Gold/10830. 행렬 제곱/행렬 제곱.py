import sys
def input(): return sys.stdin.readline().rstrip()

MOD = 1000

N, B = map(int,input().split())
M=[]
for _ in range(N):
    M.append(list(map(int,input().split())))

def expon_by_square(a,b):
    if b==1:
        return a

    n = expon_by_square(a, b//2)
    if b%2:
        return multiply_matrix(multiply_matrix(n,n),a)
    else:
        return multiply_matrix(n,n)

def multiply_matrix(a,b):
    c = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] += (a[i][k] * b[k][j]) % MOD
                
    return c

res = [[j%MOD for j in i] for i in expon_by_square(M, B)]
for i in res:
    print(*i)