import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())

cnt = 0
idx = 0

while cnt != N:
	idx += 1
	if '666' in str(idx):
		cnt += 1

print(idx)