input()
B=[0,0]
for a in map(int,input().split()):B.append(a-B[-2]-B[-1])
print(*B)