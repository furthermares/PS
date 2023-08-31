import re

print(max(re.findall('[a-zA-Z-]+', open(0).read()[:-7]), key=len).lower())