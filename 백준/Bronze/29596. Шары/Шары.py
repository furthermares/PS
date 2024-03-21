I=lambda:map(int,input().split())
X,V=I()
x,v=I()
T=int(input())
D,d=X+V*T,x+v*T
if (X-x)*(D-d)>0:print(D,V);print(d,v)
else:print(d,v);print(D,V)