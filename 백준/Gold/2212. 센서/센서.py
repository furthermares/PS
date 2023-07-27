input = __import__('sys').stdin.readline
inp = lambda: int(input())
inl = lambda: list(map(int,input().split()))

N = inp()
K = inp()
A = inl()

if K >= N:
    print(0)
    exit()

A.sort()

diff = [A[i] - A[i-1] for i in range(1,N)]
diff.sort()

print(sum(diff[:N-K]))