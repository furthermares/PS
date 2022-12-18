import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import combinations

N = int(input())
map = []
map2 = []
mines = []
for i in range(N):
    tmp = input()
    map.append(tmp)
    for j in range(N):
        if tmp[j] == "*":
            mines.append([i,j])
for i in range(N):
    map2.append(input())

dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,1,0,-1,-1,1,-1,1]
flag = False

map3=[[]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if map2[x][y] == "x":
            if map[x][y] == "*":
                flag = True
                map3[x].append("*")
            else:
                count = 0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        if map[nx][ny] == "*":
                            count += 1
                map3[x].append(count)
        else:
            map3[x].append(".")

if flag == True:
    for mX, mY in mines:
        map3[mX][mY] = "*"

for i in range(N):
    for j in range(N):
        print(map3[i][j], end="")
    print()