input()
a=sum(map(int,input().split()))
print("Right"if a>0 else"Left"if a<0 else"Stay")