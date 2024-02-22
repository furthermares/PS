X,Y,_,K=map(int,input().split())
print([X-Y,Y-X][K%2])