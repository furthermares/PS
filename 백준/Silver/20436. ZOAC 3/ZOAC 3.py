import sys
def input(): return sys.stdin.readline().rstrip()

keysl = [['z','x','c','v',None],['a','s','d','f','g'],['q','w','e','r','t']]
keysr = [['b','n','m',None,None,None],[None,'h','j','k','l',None],[None,'y','u','i','o','p']]

keysdl = {}
for i in range(3):
    for j in range(5):
        tmp = keysl[i][j]
        if tmp:
            keysdl.update({tmp:[i,j]})
keysdr = {}
for i in range(3):
    for j in range(6):
        tmp = keysr[i][j]
        if tmp:
            keysdr.update({tmp:[i,j]})

sl, sr = input().split()
str = input()

strl=""
strr=""
for i in str:
    if i in keysdl.keys():
        strl += i
    else:
        strr += i

ans=0
n_prev=keysdl[sl]
for i in strl:
    n=keysdl[i]
    ans += abs(n[0]-n_prev[0]) + abs(n[1]-n_prev[1])
    n_prev=n
n_prev=keysdr[sr]
for i in strr:
    n=keysdr[i]
    ans += abs(n[0]-n_prev[0]) + abs(n[1]-n_prev[1])
    n_prev=n

ans += len(str)

print(ans)