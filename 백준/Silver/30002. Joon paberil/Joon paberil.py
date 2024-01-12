N=int(input())
l=int(N**.5)
f=N-l*l
p=l*l+l
if N<p:x,y=f,l
else:x,y=l,p-N+l
if l%2:x,y=y,x
print(x+1,y+1)