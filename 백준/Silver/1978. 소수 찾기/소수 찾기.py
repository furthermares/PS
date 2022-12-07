import math

i=int(input())

y=input()

y=[int(b) for b in y.split()]

cnt=0

for j in range(i):

    if y[j] == 1: pass

    elif y[j] == 2: cnt+=1

    else:

        for a in range(2,int(math.sqrt(y[j]))+1):

            if y[j]%a == 0:

                break

        else:

            cnt+=1

print(cnt)