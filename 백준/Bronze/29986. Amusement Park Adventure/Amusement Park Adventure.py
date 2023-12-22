H=int(input().split()[1])
print(sum(i<=H for i in map(int,input().split())))