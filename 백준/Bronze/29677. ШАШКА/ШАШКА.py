I,i=input,int
R={}
for _ in[0]*i(I()):r,P=I().split();R[P]=i(r)
for _ in[0]*i(I()):
 A,B,X=I().split()
 S=.5if X=="0"else 1if X=="1"else 0
 EA=1+10**((R[B]-R[A])/400)
 EB=1+10**((R[A]-R[B])/400)
 R[A]=max(i(R[A]+15*(S-1/EA)),0)
 R[B]=max(i(R[B]+15*(1-S-1/EB)),0)
for P,r in sorted(R.items(),key=lambda x:(-x[1],x[0])):print(r,P)