A,B,C,D=map(int,input().split())
a,b,c,d=A,B,C,D

A%=2;C%=2
B=abs(B-D)

if B==0: print(A+C)
else: print(B)