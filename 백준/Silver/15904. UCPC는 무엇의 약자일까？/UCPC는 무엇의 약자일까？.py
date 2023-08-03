input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

import re

if re.match(".*U+.*C+.*P+.*C+.*", ins()):
    print("I love UCPC")
else:
    print("I hate UCPC")