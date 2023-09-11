input=__import__('sys').stdin.readline
ins=lambda:input().rstrip()

import re  

S = ins()

S = S[6:-7]
S = re.sub('<div +title="([\w ]*)">', r'title : \1\n', S)
S = re.sub('</p>', '\n', S)
S = re.sub('</?[\w ]*>', '', S)
S = re.sub(' {2,}', ' ', S)

print(S)