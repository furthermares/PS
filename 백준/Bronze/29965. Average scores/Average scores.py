import sys
input=sys.stdin.readline
inp=lambda:int(input())

M=[];J=[]
N = inp()
for _ in range(N):
    C, P = input().split()
    P = int(P)

    if C == "M": M.append(P)
    else: J.append(P)

m=j=0
if M: m=sum(M)/len(M)
if J: j=sum(J)/len(J)

if m>j:print("M")
elif m<j:print("J")
else:print("V")