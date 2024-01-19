class P:
 def __init__(s,x,y):s.x=x;s.y=y
 def __eq__(s,o):return s.x==o.x and s.y==o.y
 def __lt__(s,o):return s.x<o.x if s.x!=o.x else s.y<o.y
 def __hash__(s):return hash((s.x,s.y))
m=set()
a=0
for _ in[0]*int(input()):
 u,v,w,x,y,z=map(int,input().split());p=sorted([P(u,v),P(w,x),P(y,z)])
 for i in(p[0],p[1]),(p[1],p[2]),(p[0],p[2]):a+=((i[0].x-i[1].x)**2+(i[0].y-i[1].y)**2)**.5*[1,-1][i in m];m.add(i)
print(a)