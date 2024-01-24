a=[]
for _ in[0]*3:
 A,B,C,D=map(int,input().split())
 h,m=C-A,D-B
 if m<0:h-=1;m+=60
 if h<0:h+=24
 a.append((h,m))
a.sort()
for i in[0,2]:print(f"{a[i][0]}:{a[i][1]:02d}")