import sys
input = lambda: sys.stdin.readline().rstrip()

S = input()

A = [[0] * 26 for _ in range(len(S))]

for i in range(len(S)):
    for j in range(26):
        if ord(S[i])-97 == j:
            A[i][j] = A[i-1][j] + 1
        else:
            A[i][j] = A[i-1][j]

for _ in range(int(input())):
    ch, l, r = input().split()

    if not int(l):
        print(A[int(r)][ord(ch)-97])
    else:
        print(A[int(r)][ord(ch)-97] - A[int(l)-1][ord(ch)-97])