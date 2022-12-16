import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(len(A[i])):
        if j == 0:
            l = 0
            r = A[i-1][j]
        elif j == len(A[i])-1:
            l = A[i-1][j-1]
            r = 0
        else:
            l = A[i-1][j-1]
            r = A[i-1][j]
        A[i][j] += max(l,r)

print(max(A[N-1]))