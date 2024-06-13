X=int(input())
i=0
while X>i:X-=i;i+=1 
a,b=X,i-X+1
if i%2:a,b=b,a
print(f"{a}/{b}")