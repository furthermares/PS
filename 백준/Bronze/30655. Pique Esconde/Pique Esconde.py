while 1:
 N,M=map(int,input().split())
 if N==0:break
 print(*set(range(1,N+1))-{M}-{int(input()) for _ in[0]*(N-2)})