import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
d_org=[]
for _ in range(n):
    d_org.append(list(input()))

def substring(s):
    ans, temp = 1, 1

    for i in range(1, len(s)):
        if (s[i] == s[i-1]):
            temp += 1
        else:
            ans = max(ans,temp)
            temp = 1
    ans = max(ans, temp)

    return ans
    
res=0
for i in range(n):
    for j in range(n-1):
        d=[row[:] for row in d_org]
        d[i][j], d[i][j+1] = d[i][j+1], d[i][j]
        for k in range(n):
            res = max(res, substring(d[k]))
        for k in range(n):
            res = max(res, substring([row[k] for row in d]))
                
        d=[row[:] for row in d_org]
        d[j][i], d[j+1][i] = d[j+1][i], d[j][i]
        for k in range(n):
            res = max(res, substring(d[k]))
        for k in range(n):
            res = max(res, substring([row[k] for row in d]))

print(res)