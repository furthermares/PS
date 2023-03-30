import sys
input = lambda: sys.stdin.readline().rstrip()

prime = [True] * 1001
for i in range(2, 40):
    if prime[i]:
        for j in range(i*2, 1001, i):
            prime[j] = False

prime = [i for i in range(2,1001) if prime[i]]

def f(K):
    for i in prime:
        for j in prime:
            for k in prime:
                if i+j+k == K:
                    print(i,j,k)
                    return
    #print(0)    #proven to be impossible

for _ in range(int(input())):
    f(int(input()))