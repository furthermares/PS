I=lambda:map(int,input().split())
_,B,C=I()
_,b,c=I()
H,M,S=I()
t=H*B*C+M*C+S
print(t//(b*c),t%(b*c)//c,t%c)