S,T=input(),input()
v1=v2=0
for i in range(1,len(S)):
 if S[i] in"aeiou":v1=i;break
for i in range(2,len(T)+1):
 if T[-i] in"aeiou":v2=-i;break
if v1 and v2:print(S[:v1]+T[v2:])
elif v2:print(S+T[v2:])
elif v1:print(S[:v1+1]+T)
else:print(S+"o"+T)