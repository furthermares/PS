input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

import re

for _ in range(inp()):
    p = re.compile('(100+1+|01)+')

    print("YES" if p.fullmatch(ins()) else "NO")