import sys
def input(): return sys.stdin.readline().rstrip()
import cmath

# Testing. PyRival code.
def fft(a, inv=False):
    n = len(a)
    w = [cmath.rect(1, (-2 if inv else 2) * cmath.pi * i / n) for i in range(n >> 1)]
    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1
        if i & 1:
            rev[i] |= n >> 1
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    step = 2
    while step <= n:
        half, diff = step >> 1, n // step
        for i in range(0, n, step):
            pw = 0
            for j in range(i, i + half):
                v = a[j + half] * w[pw]
                a[j + half] = a[j] - v
                a[j] += v
                pw += diff
        step <<= 1

    if inv:
        for i in range(n):
            a[i] /= n

def fft_conv(a, b):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()
    a.extend([0.0] * (n - len(a)))
    b.extend([0.0] * (n - len(b)))

    fft(a), fft(b)
    for i in range(n):
        a[i] *= b[i]
    fft(a, True)

    a = [round(a[i].real) for i in range(s)]
    return a

f = [0] * 200001
for _ in range(int(input())):
    f[int(input())] = 1
f[0] = 1

g=f[:]
res = fft_conv(f,g)

cnt = 0
for _ in range(int(input())):
    if res[int(input())]>0:
        cnt += 1
print(cnt)