A=int(input())
B=int(input())
if(A+B)%2:print("Error")
elif A>1 and B>1:print("Undefined")
else:print(A//2,B//2,A%2,sep="\n")