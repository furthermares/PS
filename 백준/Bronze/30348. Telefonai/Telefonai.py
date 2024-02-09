a=[]
for _ in[0]*int(input()):
 K=input()
 if all(K[i-1]<K[i]for i in range(1,len(K))) or all(K[i-1]==K[i]for i in range(1,len(K))):a.append(int(K))
print(min(a)if a else"NERASTA")