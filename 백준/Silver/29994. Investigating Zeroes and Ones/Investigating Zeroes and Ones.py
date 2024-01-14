N=int(input())
B=[*map(int,input().split())]
o=[0]*(N+1)
e=[0]*(N+1)
for i in range(N):
 if B[i]==1:o[i+1]=e[i]+1;e[i+1]=o[i]
 else:o[i+1]=o[i];e[i+1]=e[i]+1
print(sum(o))