from collections import*
N,A,c,P=map(int,input().split()),Counter(map(int,input().split())),[[],[],[]],print
for n in N:
 for i in range(1,A[n]+1):c[i-1].append(n)
P(*c[2]);P(*c[1]);P(*c[0])