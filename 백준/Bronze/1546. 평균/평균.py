input=__import__('sys').stdin.readline

inp=lambda:int(input())

inl=lambda:list(map(int,input().split()))

N=inp()

Mi=inl()

M=max(Mi)

for i in range(N): Mi[i]/=M

print(sum(Mi)/N*100)