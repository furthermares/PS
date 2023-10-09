input=__import__('sys').stdin.readline

inm=lambda:map(int,input().split())

S1,S2=inm()

print("H" if S1/S2<0.5 else "E")