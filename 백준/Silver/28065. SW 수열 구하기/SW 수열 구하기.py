N=int(input())
A,a=range(1,N+1),[];p=N//2
if N%2:
 a.append(A[p])
 for i in range(1,p+1):a.extend([A[p-i],A[p+i]])
else:
 for i in range(p):a.extend([A[p-i-1],A[p+i]])
print(*a[::-1])