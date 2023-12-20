input=__import__('sys').stdin.readline
inp=lambda:int(input())

N=inp()
A=inp()
B=inp()
C=inp()
D=inp()

if A+C<=N<=B+D:
    print(min(N-A,D)-max(N-B,C)+1)
else:
    print(0)