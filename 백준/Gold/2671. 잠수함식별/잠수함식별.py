input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

import re

p = re.compile('(100+1+|01)+')

print("SUBMARINE" if p.fullmatch(ins()) else "NOISE")