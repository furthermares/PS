import sys
def input(): return sys.stdin.readline().rstrip()
from math import sqrt, pi, sin, cos

MAX_N = 1000001

def fft(x, w):
    n = len(x)
    if n == 1: return x
    even = x[::2]
    odd = x[1::2]
    fft(even, w*w)
    fft(odd, w*w)
    mul = complex(1,0)
    n = len(x) >> 1
    for i in range(n):
        x[i] = even[i] + mul*odd[i]
        x[i+n] = even[i] - mul*odd[i]
        mul *= w
    
def conv(A,B):
    s = len(A) + len(B) - 1
    n = 1 << s.bit_length()
    A.extend([0] * (n - len(A)))
    B.extend([0] * (n - len(B)))
    w = complex(cos(2*pi/n), sin(2*pi/n))
    fft(A, w)
    fft(B, w)
    C = [A[i]*B[i] for i in range(n)]
    fft(C, 1/w)
    for _ in range(int(input())):
        sys.stdout.write(str(round(C[int(input())].real/n))+"\n")
        
p1 = [0] * 2 + [1] * (MAX_N-2)
p2 = [0] * MAX_N
for n in range(int(sqrt(MAX_N))):
    if p1[n]:
        for i in range(n*n, MAX_N, n):
            p1[i] = 0
p2 = [0] * MAX_N
for n in range(MAX_N>>1):
    if p1[n]:
        p2[n<<1] = 1
p1[2] = 0

conv(p1, p2)