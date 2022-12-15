import sys
def input(): return sys.stdin.readline().rstrip()

s=str(input()).lower()
if s == s[::-1]:
    print(1)
else:
    print(0)