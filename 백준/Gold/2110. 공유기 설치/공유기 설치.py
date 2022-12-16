import sys
def input(): return sys.stdin.readline().rstrip()

N, C = map(int,input().split())
data = []
for _ in range(N):
    data.append(int(input()))

data.sort()
start = 1
end = data[-1] - data[0]

res = 0
while start <= end:
    mid = (start + end) // 2

    count = 1
    progress = data[0]
    for i in range(1,N):
        if data[i] >= progress + mid:
            count += 1
            progress = data[i]

    if count >= C:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)