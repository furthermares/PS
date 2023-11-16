R,F=map(int,input().split())
print("down"if R/2<F%(2*R)<R*1.5 else"up")