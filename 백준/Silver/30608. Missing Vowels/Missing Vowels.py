import sys
I,P=sys.stdin.readline,print
S,F=I().lower(),I().lower()
def X(a):
 if a not in"aeiouy":P("Different");exit()
i=j=0
while i<len(S)and j<len(F):
 if S[i]==F[j]:i+=1;j+=1;continue
 X(F[j]);j+=1
for f in F[j:]:X(f)
P("Same")