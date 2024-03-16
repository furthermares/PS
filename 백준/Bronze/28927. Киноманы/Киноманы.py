I=lambda:map(int,input().split())
T,E,F=I()
t,e,f=I()
A=T*3+E*20+F*120
a=t*3+e*20+f*120
print("Max"if A>a else"Mel"if A<a else"Draw")