import sys
def input(): return sys.stdin.readline().rstrip()

e,s,m = map(int,input().split())

chkE = 0 if e == 15 else e
chkS = 0 if s == 28 else s
chkM = 0 if m == 19 else m

ans = 1
while ans<=7980:
    if ans%15==chkE and ans%28==chkS and ans%19==chkM:
        break
    else:
        ans += 1
        
print(ans)