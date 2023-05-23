import sys
def input(): return sys.stdin.readline().rstrip()
MAX_N = 60001

MOD = 998244353
OMEGA = 3

def pow(b, e):
    r = 1
    if e & 1:
        r = b
    while e:
        e >>= 1
        b = (b * b) % MOD
        if e & 1: r = (r * b) % MOD
    return r

def ntt(a, inv=False):
    n = len(a)
    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1
        if i & 1:
            rev[i] |= n >> 1
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    ang = pow(OMEGA, (MOD - 1) // n)
    if inv:
        ang = pow(ang, MOD - 2);
    w = [0] * (n >> 1)
    w[0] = 1
    for i in range(1, n >> 1):
        w[i] = w[i-1] * ang % MOD
    
    step = 2
    while step <= n:
        half, diff = step >> 1, n // step
        for i in range(0, n, step):
            pw = 0
            for j in range(i, i + half):
                v = a[j + half] * w[pw] % MOD
                a[j + half] = (a[j] - v) % MOD
                a[j] = (a[j] + v) % MOD
                pw = (pw + diff) % MOD
        step <<= 1

    t = pow(n, MOD - 2)
    if inv:
        for i in range(n):
            a[i] = a[i] * t % MOD

def conv(a, b):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()
    a.extend([0] * (n - len(a)))
    b.extend([0] * (n - len(b)))

    ntt(a), ntt(b)
    for i in range(n):
        a[i] *= b[i]
    ntt(a, True)

    return a

U = [0] * MAX_N; input()
for i in map(int,input().split()):
    U[i+30000] = 1
M = [0] * MAX_N; input()
for i in map(int,input().split()):
    M[i+30000] = 1
L = [0] * MAX_N; input()
for i in map(int,input().split()):
    L[i+30000] = 1

res = conv(U,L)

ans = 0
for i in range(MAX_N):
    if res[2*i]:
        ans += M[i] * res[2*i]
        
print(ans)