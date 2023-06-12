M=1001;S=M*M;f=[0]*S;a=[0]*M
p=1
while p*p<S:
 for i in range(p*p,S,p):f[i]+=1
 p+=1
for i in range(S):
 if a[f[i]]==0:a[f[i]]=i
input()
for n in map(int,input().split()):print(a[n])if(n<M)*a[n]else print("Too big")