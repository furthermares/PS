N=int(input())
S=[input() for _ in range(N)]+[""]
a=[]
for i in range(N):
    if S[i]!="Present!" and S[i+1]!="Present!":
        a.append(S[i])
print(*a if a else ["No Absences"],sep="\n")