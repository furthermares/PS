import math

m,n=map(int, input().split())

for j in range(m,n+1):

    if j == 1: continue

    else:

        for a in range(2,int(math.sqrt(j))+1):

            if j%a == 0:

                break

        else:

            print(j)