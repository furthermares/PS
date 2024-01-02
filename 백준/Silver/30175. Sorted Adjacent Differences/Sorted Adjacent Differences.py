input=__import__('sys').stdin.readline
inp=lambda:int(input())
inl=lambda:[*map(int,input().split())]

for _ in range(inp()):
    N=inp()
    A=inl()
    
    A.sort()

    a=[]
    if N%2==0:
        for i in range(1,N//2+1):
            a.append(A[N//2-i])
            a.append(A[N//2+i-1])
    else:
        a.append(A[N//2])
        for i in range(1,N//2+1):
            a.append(A[N//2-i])
            a.append(A[N//2+i])
    print(*a)