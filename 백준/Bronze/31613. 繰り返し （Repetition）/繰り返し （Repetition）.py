X,N,c=int(input()),int(input()),0
while X<N:
 c+=1;R=X%3
 if R:X*=(R+1)
 else:X+=1
print(c)