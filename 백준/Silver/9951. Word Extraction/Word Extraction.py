input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

import re

ans = []

while (S := ins()) != "#":
    S = " " + S + " "
    S = S.lower()
    S = re.sub("[^\w ]", "", S)
    S = re.sub(" \d+ ", " ", S)
    S = S.split()
    S = list(set(S))
    S.sort()

    ans.append(S)
else:
    for i in range((n:=len(ans))):
        print(*ans[i], sep="\n")
        if not i == n-1:
            print()