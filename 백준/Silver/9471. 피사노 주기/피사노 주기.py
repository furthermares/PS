import sys
def input(): return sys.stdin.readline().rstrip()

def k(m):
    cnt = 1
    d1 = 1; d2 = 1

    while True:
        if d1 == 0 and d2 == 1:
            return cnt
            
        d3 = (d1 + d2) % m
        d1 = d2; d2= d3
        
        cnt += 1

for i in range(int(input())):
    Input=list(map(int,input().split()))
    print(Input[0], k(Input[1]))