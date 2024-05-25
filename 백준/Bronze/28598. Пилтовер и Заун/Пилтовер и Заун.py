X,Y,N = map(int, input().split())
print("YNEOS"[not(X>=Y)*(X-Y>=N*2)*((X-Y)%2==0)::2])