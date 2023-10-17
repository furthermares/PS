H,W,X,Y=map(float,input().split())
print(H*(X+Y)+W*(X+((Y-X)**2+H**2)**0.5))