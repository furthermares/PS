# boj.kr/1929

from math import sqrt

N = int(input())
for i in range(N+1):
    if i == 1:
        continue
    else:
        for j in range(2, int(sqrt(i))+1):
            if i%j == 0:
                break
        else:
            print(i)
