input = lambda: __import__('sys').stdin.readline().rstrip()

str = input()

A = [[0] * 26 for _ in range(len(str)+1)]

for i in range(len(str)):
    A[i][ord(str[i])-97] = 1
    for j in range(26):
        A[i][j] += A[i-1][j]

for _ in range(int(input())):
    ch, l, r = input().split()
    a, l, r = ord(ch)-97, int(l), int(r)
    print(A[r][a] - A[l-1][a])