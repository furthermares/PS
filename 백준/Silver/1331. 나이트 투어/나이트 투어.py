I=[input()for _ in[0]*36]
if len(set(I))!=36:print("Invalid");exit()
M=[(ord(I[i][0])-64,int(I[i][1]))for i in range(36)]
x=1
for i in range(36):
 t=M[i-1];a=abs(M[i][0]-t[0]);b=abs(M[i][1]-t[1])
 if not((a==1)*(b==2)or(a==2)*(b==1)):print("Invalid");break
else:print("Valid")