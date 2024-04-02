S=input()+" "
print("".join(S[i]for i in range(len(S)-1)if S[i]!=S[i+1]))