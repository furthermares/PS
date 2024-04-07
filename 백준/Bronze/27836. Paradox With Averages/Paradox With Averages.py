i=input
I=lambda:map(int,i().split())
for _ in[0]*int(i()):i();N,n=I();C=[*I()];E=[*I()];print(sum(sum(E)/n<c<sum(C)/N for c in C))