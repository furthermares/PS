a=int(input())

if not 1<=a<=1000000:

    raise ValueError("out of range")

res=0

for i in range(1,a+1):

    res+=(a//i)*i

print(res)