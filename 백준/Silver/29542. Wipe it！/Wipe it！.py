S=input()
for i in range(len(S)-1):
 if i>=len(S):break
 S=S[:i+1]+S[i+1:].replace(S[i],"")
print(S)