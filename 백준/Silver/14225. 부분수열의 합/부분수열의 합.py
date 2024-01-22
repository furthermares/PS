input()
s=0
for m in sorted([*map(int,input().split())]):
 if m<s+2:s+=m
print(s+1)