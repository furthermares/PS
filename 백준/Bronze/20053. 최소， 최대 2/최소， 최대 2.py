import sys
def input(): return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    print("{} {}".format(min(lst), max(lst)))