H,M=map(int,input().split(':'))
N=int(input())
while True:
 if M==0:N-=H
 elif M%15==0:N-=1
 if N<1:break
 M+=1
 if M==60:M=0;H+=1
 if H==13:H=1
print(f"{H:02d}:{M:02d}")