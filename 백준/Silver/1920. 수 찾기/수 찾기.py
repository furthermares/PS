import sys
input = sys.stdin.readline

input()
_set = set(map(int, input().split()))
input()
_list = list(map(int, input().split()))

print(*[1 if dt in _set else 0 for dt in _list], sep = '\n')