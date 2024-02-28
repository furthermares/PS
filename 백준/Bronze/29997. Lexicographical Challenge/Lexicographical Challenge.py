S=input()
N=int(input())
v=[sorted(S[i::N])for i in range(N)]
l=len(v)
print("".join(v[i%l][i//l]for i in range(len(S))))