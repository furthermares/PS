input=__import__('sys').stdin.readline
inp=lambda:int(input())
inl=lambda:list(map(int,input().split()))

N = inp()
A = inl()

ans = [-1] * N
stack = []

stack.append(0)
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(*ans)