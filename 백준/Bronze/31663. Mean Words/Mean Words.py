t,c,m=[0]*45,[0]*45,0
for _ in[0]*int(input()):
 S=input();m=max(m,len(S))
 for i in range(len(S)):t[i]+=ord(S[i]);c[i]+=1
print("".join(chr(t[i]//c[i])for i in range(m)))