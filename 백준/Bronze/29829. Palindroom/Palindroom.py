A,B,C,D=input().split()
if A!=D and B!=C:print("EI")
else:
 print("JAH")
 if A!=D:A=D
 elif B!=C:B=C
 print(A,B,C,D)