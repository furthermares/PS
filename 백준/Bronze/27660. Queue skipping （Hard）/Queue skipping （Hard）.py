import sys
I=sys.stdin.readline
for _ in[0]*int(I()):
 I();N,E=map(int,I().split());e=[int(I())for _ in[0]*E][::-1];n=set(range(1,N+1))
 for i in range(E):
  if len(n)==1:break
  if e[i]in n:n.remove(e[i])
 print(max(n))