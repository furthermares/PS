N=int(input())
a=b=c=0
for _ in[0]*N:
 S=input()
 if"blue"in S and"black"in S:a+=100
 elif"white"in S and"gold"in S:b+=100
 else:c+=100
print(a/N,b/N,c/N,end="\n")