X=[];Y=[]
for _ in range(N:=int(input())):x,y=map(int,input().split());X.append(x);Y.append(y)
X.sort();Y.sort()
print(X[(N-1)//2],Y[(N-1)//2])