input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

N, M = inm()

l = 1; r = M
ans = 0

for _ in range(inp()):
    pos = inp()
    
    move = 0
    if pos < l:
        move += l - pos
        l -= move
        r -= move
        ans += move
    elif l <= pos <= r:
        pass
    else:
        move += pos - r
        l += move
        r += move
        ans += move
    
print(ans)