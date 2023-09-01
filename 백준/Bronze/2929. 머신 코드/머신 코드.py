input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

import re

S = ins()
S = re.split('(?=[A-Z])', S)[1:-1]

print(sum([-len(i)%4 for i in S]))