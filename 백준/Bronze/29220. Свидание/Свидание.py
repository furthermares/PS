I=input
K,_,A=int(I()),int(I()),sorted([*map(int,I().split())])
print("YNEOS"[sum(A[1:])<K::2])