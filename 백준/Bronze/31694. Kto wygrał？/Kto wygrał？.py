I=lambda:[*map(int,input().split())]
A,B=I(),I()
if sum(A)!=sum(B):
    a=sum(A)-sum(B)
else:
    for i in range(10,-1,-1):
        if A.count(i)!=B.count(i):
            a=A.count(i)-B.count(i);break
    else:a=0
print("Algosia"if a>0else"Bajtek"if a<0else"remis")