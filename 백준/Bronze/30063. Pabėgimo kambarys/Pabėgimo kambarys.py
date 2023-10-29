N=int(input())
S=input()
import string;d=dict.fromkeys(string.ascii_uppercase,0)
for i in range(N):
 d[S[i]]+=1
 if d["R"]and d["A"]>1 and d["K"]and d["T"]and d["S"]:
  print(i+1);break