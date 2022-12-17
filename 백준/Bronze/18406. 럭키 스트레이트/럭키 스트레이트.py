import sys
def input(): return sys.stdin.readline().rstrip()

S = input()

val=0
for i in S[:int(len(S)/2)]:
    val+=int(i)
for i in S[int(len(S)/2):]:
    val-=int(i)

if val == 0:
    print("LUCKY")
else:
    print("READY")