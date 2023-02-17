import sys
def input(): return sys.stdin.readline().rstrip()

from collections import defaultdict

d = defaultdict(int)

total = 0

while True:
	tree = input()
	if not tree:
		break
		
	d[tree] += 1
	total += 1

#testing
d2 = list(d.keys())
d2.sort()

for a in d2:
	print("%s %.4f" %(a, d[a]*100/total))