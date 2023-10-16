input=__import__('sys').stdin.readline
inm=lambda:map(int,input().split())
inl=lambda:list(map(int,input().split()))

N,M = inm()
A=inl()

q = 0
len_q = 0
cnt = 0
for i in range(N):
    if q + A[i] <= M:
        q += A[i]
        len_q += 1
    else:
        for _ in range(len_q):
            print(cnt)
        cnt += 1
        q = A[i]
        len_q = 1
for _ in range(len_q):
    print(cnt)