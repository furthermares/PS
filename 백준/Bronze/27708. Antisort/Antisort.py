T=int(input())
print(T)
for _ in[0]*T:
    print(input())
    print(input())
    A=sorted(map(int,input().split()))
    print(*A[1:],A[0])