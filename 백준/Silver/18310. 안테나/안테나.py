import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

d=list(map(int,input().split()))

    

d.sort()

print(d[N//2]) if N%2==1 else print(d[N//2-1])