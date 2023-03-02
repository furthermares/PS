input = lambda: __import__('sys').stdin.readline().rstrip()

N, M = map(int,input().split())
A = [0] + list(map(int,input().split()))
cnt = [0] * (M+1)

for i in range(N):
    A[i+1] += A[i]
    cnt[A[i+1] % M] += 1

ans = cnt[0]
for i in cnt:
    ans += i*(i-1)//2
    
print(ans)