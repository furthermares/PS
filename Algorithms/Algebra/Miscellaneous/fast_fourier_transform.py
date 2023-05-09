import math

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
    
def conv(a,b):
    n = 1
    while n <= max(len(a),len(b)):
        n <<= 1
    n <<= 1
    a.extend([0]*(n - len(a)))
    b.extend([0]*(n - len(b)))
    
    w = complex(math.cos(2*math.pi/n), math.sin(2*math.pi/n))
    fft(a, w)
    fft(b, w)
    c = [a[i]*b[i] for i in range(n)]
    fft(c, 1/w)
    
    c = [round(c[i].real/n) for i in range(n)]
    return c

N, M = (map(int,input().split()))
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

res = conv(X,Y)[:N+M-1]
print(*res)

"""
Input:
9 -10 7 6
-5 4 0 -2
Output:
-45 86 -75 -20 44 -14 -12
Time Complexity: O(nlogn)
"""
