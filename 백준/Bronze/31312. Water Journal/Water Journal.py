N,A,B=map(int,input().split())
W=[int(input())for _ in[0]*(N-1)]
if(A in W)*(B in W):[print(i)for i in range(A,B+1)]
else:print(B if A in W else A if B in W else-1)