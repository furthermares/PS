input()
x=0
S=set()
for a in map(int,input().split()):
 if a>0:S.add(a)
 else:x+=-a not in S
print(x)