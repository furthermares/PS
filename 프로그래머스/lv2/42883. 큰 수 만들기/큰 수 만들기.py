input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())
ins=lambda:input().rstrip()

def solution(number, k):
    K = k
    S = number

    ans_len = len(S) - K
    stack = []

    for s in S:
        while K and stack and stack[-1] < s:
            stack.pop()
            K -= 1
        stack.append(s)

    return ''.join(stack[:ans_len])