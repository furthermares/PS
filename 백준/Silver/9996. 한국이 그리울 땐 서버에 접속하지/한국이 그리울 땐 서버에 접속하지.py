input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

import re

N = inp()
P = ins().split("*")
p = re.compile(P[0]+'.*'+P[1]+'$')

for _ in range(N):
    print("DA") if p.match(ins()) else print("NE")