S=input().upper()
d=[*set(S)]
c=[S.count(i)for i in d]
m=max(c)
print("?"if c.count(m)>1else d[c.index(m)])