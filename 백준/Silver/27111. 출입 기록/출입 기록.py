import sys
I=sys.stdin.readline
x=0
S=[False]*200001
for A,B in[map(int,I().split())for _ in[0]*int(I())]:
    if B==1:
        if S[A]:x+=1
        S[A]=True
    else:
        if not S[A]:x+=1
        S[A]=False
print(x+sum(S))