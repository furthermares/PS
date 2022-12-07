A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
#A, B, C = int(input()), int(input()), int(input())
#A, B, C = 5,8,4

if(A>=2 and A<=10000 and B>=2 and B<=10000 and C>=2 and C<=10000):
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)
else:
    raise ValueError("out of range.")