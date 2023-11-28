input=__import__('sys').stdin.readline
inp=lambda:int(input())
inl=lambda:[*map(int,input().split())]

N=inp()
V=inl()
V.sort(reverse=True)
V=[0]+V
for i in range(2,N+1):
    V[i] += V[i-1]
for _ in range(inp()):
    P=inp()-1

    s=1
    e=N

    while s<=e:
        m=(s+e)//2

        if V[m]<=P:
            s=m+1
        else:
            e=m-1
    print(s)