A=[*map(int,input().split())]
s=sum(A)
a=s//4-A[4]-A[9];b,c,d,e=A[0]-a,A[1]-a,A[2]-a,A[3]-a
print("YES"if s%4==0and a+b+c+d+e==s//4and all(i>0for i in(a,b,c,d,e))else"NO")