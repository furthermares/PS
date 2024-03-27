I,P=lambda:map(int,input().split()),print
H,B=I()
h,b=I()
s=H*3+B-h*3-b
P(1,s)if s>0else P(2,-s)if s<0else P("NO SCORE")