def f(N):q=int(N**.5);return sum(N//i for i in range(1,q+1))*2-q*q
N,M=map(int,input().split())
print(f(M)-f(N-1))