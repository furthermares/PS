I=lambda:map(int,input().split())
W,H=I()
N,A,B=I()
print(-1if(A>W)|(B>H)else-int(-N/((W//A)*(H//B))//1))