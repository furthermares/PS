S = input()

cnt=0
i_prev=S[0]
for i in S[1:]:
    if i!=i_prev: cnt+=1
    i_prev=i
        
print((cnt+1)//2)