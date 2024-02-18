N=int(input())
M=[int(input())for _ in[0]*N]
a=sum(M)/N
print("None"if M.count(3)else"Named"if a==5else"High"if a>=4.5else"Common")