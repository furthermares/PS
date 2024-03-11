N=int(input())
T=[*map(int,input().split())]
for i in range(N):T[i]=[T[i],i]
T.sort()
for i in range(N):T[i]+=[i+1]
print(*[t[2]for t in sorted(T,key=lambda x:x[1])])