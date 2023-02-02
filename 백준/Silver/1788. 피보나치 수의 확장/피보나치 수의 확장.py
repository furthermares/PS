import sys
def input(): return sys.stdin.readline().rstrip()

MOD = int(1e9)

def k(n):
    d1 = 0; d2 = 1

    for _ in range(n):          
        d3 = (d1 + d2) % MOD
        d1 = d2; d2= d3

    return d1

n = int(input())
if n == 0:
    print(0)
elif n > 0 or n%2 == 1:
    print(1)
else:
    print(-1)       

print(k(abs(n))%MOD)