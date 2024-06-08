I=[0]*21
for r in range(4):
    c=0
    for i in input().split():
        I[int(i)]=(r,c)
        c+=1
x=1
for i in range(1,20):
    a=I[i][0];b=I[i][1]
    c=I[i+1][0];d=I[i+1][1]
    if (abs(a-c)==1and abs(b-d)==2)or(abs(a-c)==2and abs(b-d)==1):x+=1
    else: break
print(x)