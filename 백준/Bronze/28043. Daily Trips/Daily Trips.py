N,H,W=map(int,input().split())
a=""
for _ in range(N):
    A,B=input().split()
    if A=='Y' or W==0:
        a+="Y "
        H-=1;W+=1
    else:
        a+="N "
    if B=='Y' or H==0:
        a+="Y\n"
        H+=1;W-=1
    else:
        a+="N\n"
print(a)