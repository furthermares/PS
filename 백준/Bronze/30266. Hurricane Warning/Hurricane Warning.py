input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

def solve():
    N = inp()
    A = list(set(ins()))
    I = [list(set(ins())) for _ in range(N)]

    ans = N
    for t in I:
        i = t[:]
        i.extend(A)
        i = list(set(i))
        if len(i) == len(t) + len(A):
            ans -= 1

    return ans

for i in range(1,(K:=inp())+1):
    print(f"Data Set {i}:")
    print(solve())
    if not i == K: print()