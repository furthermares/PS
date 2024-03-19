N,M,*t=int(input()),0,
while N:t+=[N%256];N>>=8
for i in t:M=i+M*256
print(M)