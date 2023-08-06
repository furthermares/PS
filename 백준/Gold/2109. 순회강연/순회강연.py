input=__import__('sys').stdin.readline
inp=lambda:int(input())
inl=lambda:list(map(int,input().split()))

N = inp()
PD = [inl() for _ in range(N)]

able = []
ans = 0

PD.sort(key=lambda x:x[1])

for date in range(N,0,-1):
    while PD and PD[-1][1] >= date:
        able.append(PD.pop()[0])
    if able:
        able.sort()
        ans += able.pop()

print(ans)