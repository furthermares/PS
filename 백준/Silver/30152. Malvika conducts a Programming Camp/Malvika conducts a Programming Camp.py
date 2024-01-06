input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

for _ in range(inp()):
    N,M=inm()
    if N==1: print(0)
    elif N==2: print(M)
    else: print(N-1 + (M-1)*2)