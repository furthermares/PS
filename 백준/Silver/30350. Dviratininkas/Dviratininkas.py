input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

N,K=inm()
V=[(inp(),i+1) for i in range(N)]

V.sort(reverse=True)

for i in range(K):
    print(V[i][1])