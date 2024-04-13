N=int(input())
A=[*map(int,input().split())]
x=0

chk=set()
for a in A:
    if a>0:chk.add(a)
    else:
        if -a not in chk:x+=1

print(x)