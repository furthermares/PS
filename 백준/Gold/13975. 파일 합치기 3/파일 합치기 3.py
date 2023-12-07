import heapq as H
I,P=input,H.heappop
for _ in[0]*int(I()):
 I();A=[*map(int,I().split())];H.heapify(A);a=0
 while len(A)>1:t=P(A)+P(A);a+=t;H.heappush(A,t)
 print(a)