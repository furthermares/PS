I=input
D,C,R=map(int,I().split())
c=[int(I())for i in[0]*C]
D+=sum(int(I())for i in[0]*R)
for i in c:
 if i<=D:D-=i;R+=1
 else:break
print(R)