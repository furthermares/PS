input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())

from math import factorial as fact

N,M,K = inm()

dp = [[1]*(M+1) for _ in range(N+1)]

if K > fact(N+M)//(fact(N)*fact(M)):
    print(-1)
else:
    ans = ""
    
    while N and M:
        pivot = fact(N-1+M)//(fact(N-1)*fact(M))
        if K <= pivot:
            ans += "a"
            N -= 1
        else:
            ans += "z"
            K -= pivot
            M -= 1
            
    ans += "a"*N + "z"*M
    
    print(ans)