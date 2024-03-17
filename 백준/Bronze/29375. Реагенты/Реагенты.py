input()
A=sorted([*map(int,input().split())])[::-1]
while len(A)>1:A+=[(A.pop()+A.pop())/2]
print(*A)