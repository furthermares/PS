input=__import__('sys').stdin.readline
inp=lambda:int(input())
inl=lambda:[*map(int,input().split())]

C=inp()
M=inp()
P=inl()

P.sort()

for p in P:
    if C%p==0 and C//p in P:
        print(p,C//p)
        break