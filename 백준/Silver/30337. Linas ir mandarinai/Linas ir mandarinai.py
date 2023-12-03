input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

N,K=inm()
eaten = 0
D=[inp() for _ in range(N)]
D.sort()

for expiry in D:
    day = eaten//K + 1
    if day<=expiry:
        eaten+=1
        
print(eaten)