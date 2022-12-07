import sys

g=[0]*1000001

for i in range(1,1000001):

    for j in range(i,1000001,i):

        g[j]+=i

    g[i]+=g[i-1]

for _ in range(int(sys.stdin.readline())):

    sys.stdout.write("{}\n".format(g[int(sys.stdin.readline())]))