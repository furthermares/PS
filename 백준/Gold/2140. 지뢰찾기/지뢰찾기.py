delta = ((-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0))

N = int(input())
M = [list(input()) for _ in range(N)]

ans = 0
if N > 4:
    ans += (N-4)*(N-4)
if N < 3:
    print(ans)
    exit()

for i in range(N):
    M[0][i] = int(M[0][i])
    M[-1][i] = int(M[-1][i])
for i in range(1,N-1):
    M[i][0] = int(M[i][0])
    M[i][-1] = int(M[i][-1])

for x in range(1,N-1):
    for y in range(1,N-1):
        if 1 < x < N-2 and 1 < y < N-2:
            continue

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if M[nx][ny] == 0:
                break
        else:
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if M[nx][ny] != "#":
                    M[nx][ny] -= 1
            ans += 1

print(ans)