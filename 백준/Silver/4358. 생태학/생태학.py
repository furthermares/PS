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
	
d = sorted(d.items(), key = lambda x:x[0])

for k, v in d:
	print("%s %.4f" %(k, v*100/total))
