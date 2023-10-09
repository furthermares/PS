input=__import__('sys').stdin.readline

grade = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}

ans = 0

tot = 0

for _ in range(20):

    _, C, G = input().split()

    if G == "P": continue

    C = float(C)

    ans += C * grade[G]

    tot += C

print(ans/tot)