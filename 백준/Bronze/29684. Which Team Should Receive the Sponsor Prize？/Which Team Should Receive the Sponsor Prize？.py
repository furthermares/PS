while (N:=int(input())) != 0:
    A = list(map(int,input().split()))
    mn = float('inf')
    ans = 0
    for i in range(N):
        A[i] -= 2023
        A[i] = abs(A[i])
        if A[i] < mn:
            mn = A[i]
            ans = i+1
    print(ans)