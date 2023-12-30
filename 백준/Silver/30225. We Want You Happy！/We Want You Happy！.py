input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

t=0
for _ in range(inp()):
    N,A,S,P=inm()
    if t<=A+P:
        print(N)
        t=max(t,A)+S