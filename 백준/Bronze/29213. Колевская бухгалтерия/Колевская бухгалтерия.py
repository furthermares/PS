A,B,C=map(int,input().split())
print(sum(A+i>B+j for i in range(C+1)for j in range(C+1-i)))