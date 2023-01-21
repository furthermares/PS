import sys
def input(): return sys.stdin.readline().rstrip()

def k(n):
    d1 = 0; d2 = 1

    for _ in range(n):          
        d3 = (d1 + d2) % int(1e6)
        d1 = d2; d2= d3

    return d1

print(k(int(input())%1500000)) # Pisano period of 1e6 = 1500000