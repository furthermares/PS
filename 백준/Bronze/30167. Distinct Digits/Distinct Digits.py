L,R = map(int,input().split())
for i in range(L,R+1):
    if len(set(str(i))) == len(str(i)):
        print(i)
        break
else:
    print(-1)