I=lambda:map(int,input().split())
N,M=I()
D=[*I()]
T=[*I()]
for i in range(N):
 if D[i]==T[0]:d=i
print(+(all(D[(d+i)%N]==T[i]for i in range(M))or all(D[(d-i)%N]==T[i]for i in range(M))))