S,d,n,x=input(),{"H":1,"C":12,"N":14,"O":16},1,0
for c in S[::-1]:
 if c.isalpha():x+=d[c]*n;n=1
 else:n=int(c)
print(x)