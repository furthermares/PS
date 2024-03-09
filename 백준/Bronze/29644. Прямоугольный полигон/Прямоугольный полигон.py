S,P=map(int,input().split())
if P%2==0:
    for A in range(1,30001):
        B=P//2-A
        if A*B==S:
            print(B,A)
            exit()
print(-1)