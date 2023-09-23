import sys
input=sys.stdin.readline
inp=lambda:int(input())
inl=lambda:list(map(int,input().split()))

N = inp()
S = inl()

l, r = 0, N-1
curr = 2000000000

while l < r:
    total = S[l] + S[r]
    if abs(total) < curr:
        ans = S[l], S[r]
        curr = abs(total)
    elif total < 0:
        l += 1
    else:
        r -= 1

print(*ans)