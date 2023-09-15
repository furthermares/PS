input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

import re

try:
    while (S:=ins()):
        print("She called me!!!" if re.match("^da+dd?(i|y)$", S) else "Cooing")
except:
    exit()