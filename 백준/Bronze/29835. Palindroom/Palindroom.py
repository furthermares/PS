N=int(input())
S=[*input()]
print(sum(S[i]!=S[-i-1]for i in range(N//2)))
print("".join(min(S[i],S[-i-1])for i in range(N)))