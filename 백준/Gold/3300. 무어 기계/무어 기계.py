input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

import re
import string

for _ in range(inp()):
    P = ins()
    S = ins()

    if not re.match("^" + re.sub("_", "[A-Z]+", P) + "$", S):
        print("!")
    elif re.match("^" + re.sub("_", "", P) + "$", S):
        print("_")
    else:
        for ch in string.ascii_uppercase:
            if re.match("^" + re.sub("_", ch, P) + "$", S):
                print(ch)