input = __import__('sys').stdin.readline
inm = lambda: map(int,input().split())

i = 0
while True:
    i += 1
    L,P,V = inm()
    if not (L or P or V):
        break

    ans = V // P * L + min(V % P, L)
    print(f"Case {i}: {ans}")