I=input
I()
print(sorted([V:=int(I())]+[*map(int,I().split())])[::-1].index(V)+1)