N,M,K=map(int,input().split())
v=[*map(int,input().split())]
v.sort()
print(sum(v[::-1][:min(M+K,N)])*100/sum(v))