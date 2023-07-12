input = __import__('sys').stdin.readline
inm = lambda: map(int,input().split())
from math import gcd

D,K = inm()

ans = 1
if D%4==2 and K%2==0 and K>2:
    ans *= 2

while True:
    g = gcd(D,K)
    if g == 1:
        break
    ans *= g
    K //= g
    
print(ans * D)
