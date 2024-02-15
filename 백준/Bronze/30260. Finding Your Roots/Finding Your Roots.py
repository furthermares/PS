I=input
for K in range(int(I())):
 L,n=map(int,I().split())
 P,a,L=[*map(int,I().split())],1,L-1
 while P[L]:L,a=P[L]-1,a+1
 print(f"Data Set {K+1}:\n{a}\n")