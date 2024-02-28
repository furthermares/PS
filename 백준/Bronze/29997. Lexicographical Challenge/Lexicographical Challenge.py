input=__import__('sys').stdin.readline
S=input().rstrip()
N=int(input())

v=[]
for i in range(N):
    v.append(sorted(S[i::N]))
l=len(v)
for i in range(len(S)):
    print(v[i%l][i//l],end="")