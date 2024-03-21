I,P=lambda:map(int,input().split()),print
X,V=I()
x,v=I()
T=int(input())
D,d=X+V*T,x+v*T
if (X-x)*(D-d)>0:P(D,V);P(d,v)
else:P(d,v);P(D,V)