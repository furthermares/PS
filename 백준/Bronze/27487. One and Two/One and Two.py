from math import*
for _ in[0]*int(input()):
    N=int(input())
    A=[*map(int,input().split())]

    l,r=1,prod(A)
    for i in range(N-1):
        l*=A[i]
        r//=A[i]
        if l==r:
            print(i+1)
            break
    else:
        print(-1)