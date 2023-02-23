import sys
def input(): return sys.stdin.readline().rstrip()

N, L = list(map(int,input().split()))
S = list(map(int,input().split()))

S.sort()

cnt = 0
pos = 0
for i in S:
    if i < pos:
        continue
    pos = i + L
    cnt += 1

print(cnt)