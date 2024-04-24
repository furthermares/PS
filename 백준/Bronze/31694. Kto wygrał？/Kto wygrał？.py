I=lambda:[*map(int,input().split())]
A,B=I(),I()
x=sum(A)-sum(B)
if x==0:
 for i in range(10,-1,-1):
  if x:=A.count(i)-B.count(i):break
print("Algosia"if x>0else"Bajtek"if x<0else"remis")