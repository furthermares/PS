input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

import re

p = re.compile("<B>([^<>]*)</B>|<I>([^<>]*)</I>|<A HREF=http://[^<>]*\.com>([^<>]*)</A>")

for _ in range(inp()):
    S = ins()

    if S.startswith("<HTML><BODY>") and S.endswith("</BODY></HTML>"):
        S = S[len("<HTML><BODY>"):-len("</BODY></HTML>")]
        while re.search(p, S):
            S = re.sub(p, r"\1\2\3", S)

    if not any(i in S for i in ("<", ">")):
        print("Syntax Included")
    else:
        print("No Syntax Included")