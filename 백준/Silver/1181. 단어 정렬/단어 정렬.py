import sys
def input(): return sys.stdin.readline().rstrip()

S = set()
for _ in range(int(input())):
    S.add(input())
S = list(S)
S.sort()
S.sort(key=len)

print(*S, sep="\n")