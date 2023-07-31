input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

def A1Z26(S):
    return [ord(ch) - 64 for ch in S]
    
N = inp()
eq = [A1Z26(ins()) for _ in range(N)]

mask = [0] * 27

for i in range(N):
    for j in range(len(eq[i])):
        mask[eq[i][j]] += 10 ** (len(eq[i])-j-1)

mask.sort(reverse=True)

num = 9
ans = 0
for i in mask:
    if i:
        ans += i * num
        num -= 1

print(ans)