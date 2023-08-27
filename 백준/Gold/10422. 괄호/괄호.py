input=__import__('sys').stdin.readline
inp=lambda:int(input())

from math import factorial as fact
MOD = int(1e9)+7

def catalan(n):
    return fact(2*n) // (fact(n) * fact(n+1))

for _ in range(inp()):
    L = inp()

    if L & 1:
        print(0)
    else:
        print(catalan(L//2) % MOD)