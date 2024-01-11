H,D,T=map(int,input().split())
h,d,t=map(int,input().split())
i=0
a=0
while not a:
 if i%T==0:h-=D
 if i%t==0:H-=d
 if H<1and h<1:a="draw"
 elif H<1:a="player two"
 elif h<1:a="player one"
 i+=1
print(a)