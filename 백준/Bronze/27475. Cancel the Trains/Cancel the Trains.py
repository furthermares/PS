I=lambda:[*map(int,input().split())]
for _ in[0]*int(input()):I();N,M=I(),I();print(sum(n==m for n in N for m in M))