A=input()
B=input()
print("".join(max(A[i],B[i])for i in range(len(A))))