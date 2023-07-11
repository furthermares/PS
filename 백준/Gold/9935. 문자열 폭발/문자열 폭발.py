input = __import__('sys').stdin.readline
insl = lambda: list(input()[:-1])

S = insl()
T = insl()

stack = []
len_T = len(T)

for i in range(len(S)):
    stack.append(S[i])
    if stack[-len_T:] == T:
        for _ in range(len_T):
            stack.pop()

print(''.join(stack)) if stack else print('FRULA')