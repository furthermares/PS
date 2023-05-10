import sys
def input(): return sys.stdin.readline().rstrip()

while True:
    S = list(map(int,input().split()))
    S.sort()
    a,b,c = S
    if not (a or b or c):
        break
    if a*a + b*b == c*c:
        print("right")
    else:
        print("wrong")