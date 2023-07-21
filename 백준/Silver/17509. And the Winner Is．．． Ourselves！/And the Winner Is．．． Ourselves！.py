input = __import__('sys').stdin.readline
inl = lambda: list(map(int,input().split()))

LEN = 11

DV = [inl() for _ in range(LEN)]
DV.sort()

t = p = 0
for i in range(LEN):
    t += DV[i][0]
    p += t + 20 * DV[i][1]

print(p)