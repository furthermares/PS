input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

N=inp()
S=ins()
st=a=0

for i in range(N):
    if S[i]=="(":st+=1
    else:st-=1
    if st<0 or st==0 and S[i]=="(":a+=1

print(-1 if st else a)