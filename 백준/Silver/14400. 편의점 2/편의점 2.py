X=[];Y=[]
for _ in range(N:=int(input())):x,y=map(int,input().split());X.append(x);Y.append(y)
X.sort();Y.sort()
print(sum(abs(X[i]-X[(N-1)//2])+abs(Y[i]-Y[(N-1)//2])for i in range(N)))