N,S,mn,mx,ans=int(input()),input().rstrip(),{},{},0
p=[0]*(N+1)
for i in range(N):p[i+1]=p[i];p[i+1]+=1if S[i]=="+"else-1
for i in range(N+1):
 if p[i]not in mn:mn[p[i]]=i
 elif i<mn[p[i]]:mn[p[i]]=i
 if p[i]not in mx:mx[p[i]]=i
 elif i>mx[p[i]]:mx[p[i]]=i
 ans=max(ans,mx[p[i]]-mn[p[i]])
print(ans)