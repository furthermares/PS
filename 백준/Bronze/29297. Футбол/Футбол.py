for _ in[0]*int(input()):
 A,B=map(int,input().split(':'));L=D=0
 for i in range(10):
  for j in range(10):
   if A+i>B+j:L+=1
   elif A+i<B+j:D+=1
   elif i>B:L+=1
   elif i<B:D+=1
 print(L,D)