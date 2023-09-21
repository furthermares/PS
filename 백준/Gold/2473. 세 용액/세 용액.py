import sys
input=sys.stdin.readline
inp=lambda:int(input())
inl=lambda:list(map(int,input().split()))

N = inp()
S = sorted(inl())

curr = 3000000000

for i in range(N-2):
    l, r = i+1, N-1
    while l < r:
        total = S[i] + S[l] + S[r]
        if abs(total) < curr:
            ans = S[i], S[l], S[r]
            curr = abs(total)
        elif total < 0:
            l += 1
        else:
            r -= 1

print(*ans)