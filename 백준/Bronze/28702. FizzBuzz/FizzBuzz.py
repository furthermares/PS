a,b,c=input(),input(),input()
n=int(a)+2 if a.isdigit()else-~int(b)if b.isdigit()else int(c)
print("Fizz"*(n%3==2)+"Buzz"*(n%5==4)or-~n)