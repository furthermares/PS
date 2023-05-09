import sys
def input(): return sys.stdin.readline().rstrip()
import math

MAX_N = 1000002

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
    n = 1
    while n <= max(len(A),len(B)):
        n <<= 1
    n <<= 1
    A.extend([0]*(n - len(A)))
    B.extend([0]*(n - len(B)))
    w = complex(math.cos(2*math.pi/n), math.sin(2*math.pi/n))
    fft(A, w)
    fft(B, w)
    C = [A[i]*B[i] for i in range(n)]
    fft(C, 1/w)
    for _ in range(int(input())):
        print(round(C[int(input())].real/n))
        
p1 = [0] * 2 + [1] * (MAX_N-2)
p2 = [0] * MAX_N
p = []
for n in range(MAX_N):
    if p1[n]:
        p.append(n)
        for i in range(n*n, MAX_N, n):
            p1[i] = 0
p1[2] = 0

p2 = [0] * MAX_N
for n in p:
    if n > MAX_N>>1:
        break
    p2[n<<1] = 1

conv(p1, p2)