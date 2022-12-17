import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
S = input()

cnt = 0
for i in range(N-1):
    if S[i] != S[i+1]:
        cnt += 1

if S[0] == S[-1]:
    print(cnt//2+1)
else:
    print((cnt+1)//2+1)