input=__import__('sys').stdin.readline
inp=lambda:int(input())

N=inp()
DP=[]
P={}
for _ in range(N):
    D,Pi = input().split()
    Pi=int(Pi)
    P[Pi]=0
    DP.append((D,Pi))

for D,Pi in DP:
    if D=="G":
        for i in P:
            if i >= Pi:
                P[i]+=1
    else:
        for i in P:
            if i <= Pi:
                P[i]+=1

print(N-max(P.values()))
