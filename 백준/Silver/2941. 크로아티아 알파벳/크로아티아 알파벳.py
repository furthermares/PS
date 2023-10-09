input=__import__('sys').stdin.readline

ins=lambda:input().rstrip()

import re

S = ins()

for i in ("c=","c-","dz=","d-","lj","nj","s=","z="):

    S = re.sub(i, "0", S)

print(len(S))