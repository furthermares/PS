input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

def A1Z26(S):
    return [ord(ch) - 64 for ch in S]
    
N = inp()
S = [A1Z26(ins()) for _ in range(N)]

mask = [[0, i] for i in range(10)]

for s in S:
    for i in range(len(s)):
        mask[s[i]-1][0] += 10 ** (len(s)-i-1)

mask.sort()

front = [False] * 10
for s in S:
    front[s[0]-1] = True
    
for i in range(10):    
    if not front[mask[i][1]]:
        mask[i][0] = 0
        break

mask.sort()

num = 0
ans = 0
for i, j in mask:
    ans += i * num
    num += 1

print(ans)