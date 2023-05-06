from cmath import exp, pi

def fft(x, inv=False):
    n = len(x)
    if n == 1: return x
    even = fft(x[0::2], inv)
    odd =  fft(x[1::2], inv)
    if not inv:
        T= [exp(-2j*pi*k/n)*odd[k] for k in range(n//2)]
    else:
        T= [exp( 2j*pi*k/n)*odd[k] for k in range(n//2)]
    return [even[k] + T[k] for k in range(n//2)] + \
           [even[k] - T[k] for k in range(n//2)]
    
def conv(A,B):
    n = 1
    while n <= max(len(A),len(B)):
        n <<= 1
    A += [0]*(n - len(A))
    B += [0]*(n - len(B))
    AT = fft(A)
    BT = fft(B)
    C = [AT[i]*BT[i] for i in range(n)]
    return [round((a/n).real) for a in fft(C, True)]

X = list(map(int,input().split()))
Y = list(map(int,input().split()))

print(conv(X,Y)[:len(X)+len(Y)-1])

"""
(Polynomial multiplication using FFT)
(!
Input:
9 -10 7 6
-5 4 0 -2
Output:
-45 86 -75 -20 44 -14 -12 0
Time Complexity: O(nlogn)
"""
