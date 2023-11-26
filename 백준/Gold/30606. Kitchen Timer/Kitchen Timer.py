input=__import__('sys').stdin.readline
inp=lambda:int(input())

l=[]
i=2
while i <= 10**18:
    l.append(i-1)
    i*=2

for _ in range(inp()):
    X=inp()

    ans = 0
    for i in l[::-1]:
        ans += X//i
        X %= i
    print(ans-1)