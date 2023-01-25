import sys
def input(): return sys.stdin.readline().rstrip()

MOD = 1000000007

def k(n):
    d1 = 0; d2 = 1

    for _ in range(n):          
        d3 = (d1 + d2) % MOD
        d1 = d2; d2= d3

    return d1

print(k(int(input()))%MOD)