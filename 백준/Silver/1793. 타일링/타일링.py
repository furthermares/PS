import sys
def input(): return sys.stdin.readline().rstrip()

d = [1]+[1]+[0]*249
for i in range(2,251):
    d[i] = (d[i-1] + d[i-2]*2)
    
while(True):
    try: N = int(input())
    except: break
    print(d[N])