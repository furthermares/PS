import math as M
N=int(input())
S=sorted([*map(int,input().split())])
print("%.3f"%((S[0]*S[1]+S[-2]*S[-1]+sum(S[i]*S[i+2]for i in range(N-2)))*M.sin(M.pi*2/N)/2))