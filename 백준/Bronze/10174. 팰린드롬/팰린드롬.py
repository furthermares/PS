#import sys
#def input(): return sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    s=str(input()).lower()
    if s == s[::-1]:
        print('Yes')
    else:
        print('No')