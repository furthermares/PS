import sys
def input(): return sys.stdin.readline().rstrip()

R, C = map(int,input().split())
map=[[]*(C+1) for _ in range(R+1)]
map[0] = "."*(C+2)
for i in range(1,R+1):
    map[i] = "."
    map[i] += input()
    map[i] += "."
map += ["."*(C+2)]

map_new = [""*C for _ in range(R)]

for i in range(1,R+1):
    for j in range(1,C+1):
        if map[i][j] == "X":
            if (map[i-1][j] + map[i+1][j] + map[i][j-1] + map[i][j+1]).count(".") >= 3:
                map_new[i-1]+="."
            else:
                map_new[i-1]+="X"
        else:
            map_new[i-1]+="."

while(True):
    if "X" not in map_new[0]:
        map_new.pop(0)
    elif "X" not in map_new[-1]:
        map_new.pop(-1)
    else:
        break
while(True):
    if "X" not in [i[0] for i in map_new]:
        map_new=[i[1:] for i in map_new]
    elif "X" not in[i[-1] for i in map_new]:
        map_new=[i[:-1] for i in map_new]
    else:
        break

for i in range(len(map_new)):
    print(map_new[i])