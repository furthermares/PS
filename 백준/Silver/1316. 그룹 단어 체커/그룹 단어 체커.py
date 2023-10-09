input=__import__('sys').stdin.readline

inp=lambda:int(input())

ins=lambda:input().rstrip()

ans = inp()

for _ in range(ans):

    S = ins()

    

    prev = None

    his = set()

    

    for i in S:

        if i != prev:

            prev = i

            

            if i in his:

                ans -= 1

                break

            his.add(i)

print(ans)