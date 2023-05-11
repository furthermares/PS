import sys
def input(): return sys.stdin.readline().rstrip()
from math import sqrt, pi, sin, cos

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
    
def conv(A):
    n = 1 << len(A).bit_length()
    A.extend([0] * (n - len(A)))
    w = complex(cos(2*pi/n), sin(2*pi/n))
    fft(A, w)
    A = [A[i]*A[i] for i in range(n)]
    fft(A, 1/w)
    for _ in range(int(input())):
        x = int(input())
        if x == 4:
            sys.stdout.write('1' + '\n')
        else:
            sys.stdout.write(str(round(A[(x>>1)-1].real/n)+1 >> 1)+"\n")
    
MAX_N = 1000000

p1 = [0] * 2 + [1] * (MAX_N-2)
for n in range(1,int(sqrt(MAX_N))):
    if p1[n]:
        for i in range(n*n, MAX_N, n):
            p1[i] = 0
p = [0] * (MAX_N)
for i in range(3, MAX_N, 2):
    if p1[i]:
        p[i>>1] = 1

conv(p)