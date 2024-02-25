while(S:=input())!="#":
 S,x=sorted(S,key=str.swapcase),0
 for i in range(len(S)):
  if S[i].isalpha():x=i;break
 print("".join(S[x:]+S[:x]))