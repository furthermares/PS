N,D=map(int,input().split())
d=-D+2
print("+---------------------+")
print("|",end="")
while True:
    if d>N:
        if (d+D-1)%7==1:
            break
        while (d+D-1)%7!=1:
            print("...",end="")
            d+=1
        print("|",end="\n")
        break

    if (d+D-1)%7==1 and d+D-1>6:
        print("|",end="")
        
    if d>0:
        print("."if d>9 else "..",end="")
        print(d,end="")
    else:
        print("...",end="")
        
    if (d+D-1)%7==0 and d+D-1>6:
        print("|",end="\n")
        
    d+=1
print("+---------------------+")