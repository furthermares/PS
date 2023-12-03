import re
I=input
S,F,p=I().rstrip().lower(),I().rstrip().lower(),"[aeiouy]?"
print(["Different","Same"][bool(re.match(fr"{p+p.join(S)+p}",F))])
