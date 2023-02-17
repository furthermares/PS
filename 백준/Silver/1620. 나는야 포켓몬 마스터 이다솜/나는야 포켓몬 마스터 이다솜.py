import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
dict = {}

for i in range(1,N+1):
	str = input()
	dict[i] = str
	dict[str] = i

for _ in range(M):
	test = input()
	if test.isdigit():
		print(dict[int(test)])
	else:
		print(dict[test])