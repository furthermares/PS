import sys
def input(): return sys.stdin.readline().rstrip()

def expon_by_square(a,b,c):
    if b==1:
        return a%c

    n = expon_by_square(a, b//2, c)
    if b%2:
        return (n*n*a)%c
    else:
        return (n*n)%c

A,B,C = map(int,input().split())
print(expon_by_square(A,B,C))