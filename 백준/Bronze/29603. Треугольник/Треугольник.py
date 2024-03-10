P=print
I=lambda:map(int,input().split())
A,B=I()
C,D=I()
E,F=I()
P(A+E-C,B+F-D)
P(A+C-E,B+D-F)
P(C+E-A,D+F-B)