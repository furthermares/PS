import re

S = __import__('sys').stdin.readlines()

for s in S:
    while "BUG" in s:
        s = re.sub("BUG","",s)
    print(s,end="")