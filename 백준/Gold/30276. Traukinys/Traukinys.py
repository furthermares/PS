I=lambda:map(int,input().split())
N,K=I()
A=I()
a=d=0
for i in A:d+=K-i;a+=abs(d)
print(a)