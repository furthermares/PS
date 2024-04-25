R,C=map(int,input().split())
print(R*(R-1)**(C-1)%998244353)