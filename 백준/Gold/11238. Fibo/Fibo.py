import sys
def input(): return sys.stdin.readline().rstrip()

from math import gcd

MOD = 1000000007

M = [[1,1],[1,0]]
def expon_by_square(a,b):
    if b==1:
        return a

    n = expon_by_square(a, b//2)
    if b%2:
        return multiply_matrix(multiply_matrix(n,n),a)
    else:
        return multiply_matrix(n,n)

def multiply_matrix(a,b):
    c = [[0]*2 for _ in range(2)]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= MOD
                
    return c

for _ in range(int(input())):
    n, m = map(int,input().split())
    print(expon_by_square(M,gcd(n, m))[0][1] % MOD)