import sys
input = sys.stdin.readline
inp = lambda: int(input())
ins = lambda: input().rstrip()
sys.setrecursionlimit(10**6)

MOD = 1000000007

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1) % MOD

def LCP_idx(S, T):
    idx = 0
    while idx < len(S) and idx < len(T) and S[idx] == T[idx]:
        idx += 1
    return idx

N = inp()
S = [ins() for _ in range(N)]
S.sort()

def solve(Si, level):
    if len(Si) == 1:
        return 1

    ith_letters = dict()
    for i in Si:
        if len(S[i]) <= level:
            ith_letters[''] = [i]
        else:
            ith_letters.setdefault(S[i][level],[]).append(i)
  
    res = factorial(len(ith_letters.keys()))
    for v in ith_letters.values():
        res *= solve(v, level+1)
        res %= MOD
    return res

print(solve(range(N), 0))