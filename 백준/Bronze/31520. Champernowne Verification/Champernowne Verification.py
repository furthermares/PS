N=input()
print(N[-1]if N in("123456789"[:i+1]for i in range(9))else-1)