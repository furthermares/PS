input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())
ins=lambda:input().rstrip()

N,K = inm()
S = ins()

ans_len = N - K
stack = []

for s in S:
    while K and stack and stack[-1] < s:
        stack.pop()
        K -= 1
    stack.append(s)

print(''.join(stack[:ans_len]))