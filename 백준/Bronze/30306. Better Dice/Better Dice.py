input=__import__('sys').stdin.readline

inp=lambda:int(input())

inl=lambda:list(map(int,input().split()))

N = inp()

A=inl()

B=inl()

cnt=cbt=0

for i in range(N):

    for j in range(N):

        if A[i]>B[j]:

            cnt += 1

        elif A[i]<B[j]:

            cbt += 1

print("tie" if cnt == cbt else "first" if cnt > cbt else "second")