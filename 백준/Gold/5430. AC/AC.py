import sys
def input(): return sys.stdin.readline().rstrip()

from collections import deque

for _ in range(int(input())):
	P = input()
	N = int(input())
	X = deque(map(str,input()[1:-1].split(',')))

	P = P.replace("RR","")

	flag_R = False
	
	if N == 0 and "D" in P:
		print("error")
	else:
		for i in P:
			if i == "R":
				if flag_R:
					flag_R = False
				else:
					flag_R = True
			else:
				if(len(X) == 0):
					print("error")
					break

				if not flag_R:
					X.popleft()
				else:
					X.pop()
		else:
			if flag_R:
				X.reverse()
			print("[" + ",".join(X) + "]")