input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())

V,K=inm()
A=[0]+[1]*V

for i in range(V,0,-1):
    if i-K<1:break
    if not A[i]:continue
    A[i-K]-=1
    
print(sum(A))
print(*[i for i in range(V,0,-1) if A[i]],sep="\n")