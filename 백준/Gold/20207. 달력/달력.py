input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

MAX = 365
board = [0] * (MAX+2)

for _ in range(inp()):
    S, E = inm()
    board[S] += 1
    board[E+1] -= 1

max_height = 0
length = 0
height = 0
ans = 0
for i in range(MAX+2):
    height += board[i]
    if height:
        max_height = max(height, max_height)
        length += 1
    else:
        ans += length * max_height
        max_height = 0
        length = 0

print(ans)