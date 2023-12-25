N=int(input())
print("Happy"if sum(a%2for a in map(int,input().split()))<N/2else"Sad")