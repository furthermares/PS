for _ in range(int(input())):
 input();a=0
 for i in map(int,input().split()):a+=1;a+=i==a
 print(a)