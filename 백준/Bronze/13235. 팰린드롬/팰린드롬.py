import sys
def input(): return sys.stdin.readline().rstrip()

s=input()
if s == s[::-1]:
    print('true')
else:
    print('false')