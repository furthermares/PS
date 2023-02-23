import sys
def input(): return sys.stdin.readline().rstrip()
import bisect

N = int(input())
A = sorted(list(map(int,input().split())))
M = int(input())
B = map(int,input().split())

ans = []
for i in B:
    ans.append(bisect.bisect_right(A,i) - bisect.bisect_left(A,i))

print(*ans)