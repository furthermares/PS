input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

A=[ins() for _ in range(inp())]
for _ in range(inp()):
    L,R = map(int,input().split())
    print(*A[L-1:R],sep="\n")