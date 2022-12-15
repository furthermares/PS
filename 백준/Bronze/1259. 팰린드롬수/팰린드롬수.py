import sys
def input(): return sys.stdin.readline().rstrip()

while(True):
    s=str(input())
    if s == '0':
        break

    if s == s[::-1]:
        print('yes')
    else:
        print('no')