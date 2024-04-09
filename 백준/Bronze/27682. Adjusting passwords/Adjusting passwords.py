I=input
for _ in[0]*int(I()):
 I();P,Q=I(),I();p,q=len(P),len(Q)
 if P==Q:print("*");continue
 for i in range(r:=min(p,q)):
  if P[i]!=Q[i]:x=i;break
 else:x=r
 print(f"*{P}*"if(q>x*2)else"<"*(q-x)+P[x:]+"*")