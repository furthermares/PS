A=set(tuple(map(int,input().split()))for _ in[0]*[*map(int,input().split())][1])
print(sum(sum((x+(-1,1,0,0,0,0)[i],y+(0,0,-1,1,0,0)[i],z+(0,0,0,0,-1,1)[i])in A for i in range(6))==6for x,y,z in A))