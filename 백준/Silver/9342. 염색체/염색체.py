input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

import re

p = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(inp()):
    print("Infected!") if p.match(ins()) else print("Good")