import sys, math

MAX=1000000

primes=[False]*2+[True]*(MAX-1)

for i in range(2, int(math.sqrt(MAX))+1):

    if primes[i]:

        for k in range(i ** 2, MAX+1, i):

            primes[k] = False

while(True):

    i = int(sys.stdin.readline())

    if(i==0): break

    for a in range(3,len(primes)//2):

        if primes[a] and primes[i - a]:

            sys.stdout.write("{} = {} + {}\n".format(i,a,i-a))

            break