input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

S = ins()

ans = 0
for i in range(len(S)-3):
    if S[i:i+4] == 'kick':
        ans += 1

print(ans)