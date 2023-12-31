input=__import__('sys').stdin.readline
inp=lambda:int(input())

N=inp()
H=[inp() for _ in range(N)]

a=0
p=H[0]
for i in range(1,N):
    if H[i]-H[i-1]<=0:
        a=max(a,H[i-1]-p)
        p=H[i]
a=max(a,H[-1]-p)

print(a)