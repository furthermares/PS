import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
S = [list(map(int, input().split())) for _ in range(N*N)]

G = [[0] * N for _ in range(N)]
dx,dy = [-1,1,0,0],[0,0,-1,1]

def get_seat(cnt):
    max_cnt = max(map(max, cnt))
    seats = []
    for x in range(N):
        for y in range(N):
            if cnt[x][y] == max_cnt:
                seats.append((x, y))
    return seats

def get_adj_favs(a):
    cnt = [[-1] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if G[x][y] == 0:
                cnt[x][y] += 1
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        for fav in S[a][1:]:
                            if G[nx][ny] == fav:
                                cnt[x][y] += 1
    return get_seat(cnt)

def print_adj_favs_score():
    cnt = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            a = G[x][y]
            for i in range(N*N):
                if S[i][0] == a:
                    favs = S[i][1:]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    for fav in favs:
                        if G[nx][ny] == fav:
                            cnt[x][y] += 1

    score = 0
    for x in range(N):
        for y in range(N):
            target = cnt[x][y]
            if target == 4:
                score += 1000
            elif target == 3:
                score += 100
            elif target == 2:
                score += 10
            elif target == 1:
                score += 1
    print(score)

def get_adj_empty(seats):
    cnt = [[-1] * N for _ in range(N)]
    for x, y in seats:
        if G[x][y] == 0:
            cnt[x][y] += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if G[nx][ny] == 0:
                        cnt[x][y] += 1
    return get_seat(cnt)

for i in range(N*N):
    seats = get_adj_favs(i)
    if len(seats) != 1:
        seats = get_adj_empty(seats)
    G[seats[0][0]][seats[0][1]] = S[i][0]

print_adj_favs_score()