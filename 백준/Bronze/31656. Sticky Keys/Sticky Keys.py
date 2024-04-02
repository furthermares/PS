S=input()
print(S[0],end="")
for i in range(1,len(S)):
    if S[i-1]!=S[i]:print(S[i],end="")