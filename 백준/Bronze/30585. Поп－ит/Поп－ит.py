H,W=map(int,input().split())
S=""
for _ in range(H):S+=input()
x=S.count('0')
print(x if x<=(H*W)/2 else H*W-x)