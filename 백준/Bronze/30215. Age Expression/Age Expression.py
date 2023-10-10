input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())
O,A,K=inm()
ans = False
O -= A + K
for i in range(O//A+1):
    if not (O - A*i) % K:
        ans = True
        break

print(int(ans))