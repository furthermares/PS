input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

def base36encode(n):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ret = []

    if n < 36:
        return alphabet[n]
    while n:
        n, i = divmod(n, 36)
        ret.append(alphabet[i])

    return ''.join(ret[::-1])
    
def base36decode(n):
    return int(n, 36)

S = [ins() for _ in range(inp())]
K = inp()

mask = [[0, i] for i in range(36)]

for s in S:
    for i in range(len(s)):
        mask[base36decode(s[i])][0] += 36 ** (len(s)-i-1)

weight = [[mask[i][0] * (35-i), i] for i in range(36)]
weight.sort(reverse=True)

ans = sum(mask[weight[i][1]][0] * (35 if i < K else weight[i][1]) for i in range(36))
print(base36encode(ans))