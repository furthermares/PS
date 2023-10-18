import math
a=math.ceil(int(input())/2)-len([i for i in map(int,input().split())if i==1])
print(a if a>0else 0)