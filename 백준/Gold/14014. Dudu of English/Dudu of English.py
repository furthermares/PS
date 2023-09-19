input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

import re

S = ""
for i in range(inp()):
    S += " " + ins()

S = S.lower()
S2 = ""
for word in S.split():
    if word in {"to", "into", "onto", "above", "below", "from", "by", "is", "at"}:
        S2 += "of "
        continue
    
    cnt = len(re.findall("[aeiou]", word)) // 2
    if cnt == 0:
        cnt = -1
    S2 += re.sub("[aeiou]", "", word, cnt) + " "
S2 = re.sub("[^a-zA-Z ]", "", S2)

S3 = ""
cnt = 0
for word in S2.split():
    if len(S3) - cnt > 20:
        print(S3[:-1])
        S3 = ""
        cnt = 0
    S3 += word + " "
    cnt += 1
if S3:
    print(S3[:-1])