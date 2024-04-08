i=input
I=lambda:map(int,i().split())
for _ in[0]*int(i()):i();N,n=I();C=[*I()];c=sum(C)/N;e=sum(I())/n;print(sum(e<j<c for j in C))