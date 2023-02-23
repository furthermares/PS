import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = set([input() for _ in range(N)])
B = set([input() for _ in range(M)])

lst = sorted(A & B)
print(len(lst))
print(*lst, sep="\n")