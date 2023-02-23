import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = sorted(list(map(int,input().split())))
M = int(input())
B = map(int,input().split())

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

ans = []
for i in B:
    if binary_search(A, i, 0, N-1) != None:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)