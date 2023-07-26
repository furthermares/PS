input = __import__('sys').stdin.readline
inp = lambda: int(input())
inm = lambda: map(int,input().split())

L,W,H = inm()
AB = [tuple(inm()) for _ in range(inp())]

ans = used = 0
for Ai, Bi in AB[::-1]:
    used <<= 3
    A = 2**Ai
    cnt = min(Bi, (L//A) * (W//A) * (H//A) - used)
    ans += cnt
    used += cnt

print(ans) if used == L*W*H else print(-1)