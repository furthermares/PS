for t in range(int(input())):
 if t:input()
 M=[input()for _ in[0]*5]
 for i in range(5):
  for j in range(5):
   if M[i][j]=="k":
    for x,y in(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2):
     if(0<=i+x<5)and(0<=j+y<5)and(M[i+x][j+y]=="k"):print("in",end="");break
    else:break
 else:print("valid")