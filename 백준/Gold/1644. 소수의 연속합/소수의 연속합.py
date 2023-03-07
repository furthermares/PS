import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

prime_idx = [False, False] + [True] * (N-1)
p = 2
while (p*p <= N):
    if prime_idx[p]:
        for i in range(p*p, N+1, p):
            prime_idx[i] = False
    p += 1
prime = [i for i, j in enumerate(prime_idx) if j == True and i >= 2]

l, r = 0, 1
cnt = 0
while r <= len(prime):
    total = sum(prime[l:r])
    if total == N:
        cnt += 1
        r += 1
    elif total > N:
        l += 1
    else:
        r += 1

print(cnt)
