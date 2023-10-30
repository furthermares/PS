input=__import__('sys').stdin.readline
a=""
for _ in range(int(input())):
 S=[input().rstrip() for _ in range(8)]
 if S[5]==".##...##.":a+="0"
 elif S[5]=="....##...":a+="1"
 elif S[5]=="##.......":a+="2"
 elif S[5]=="......##.":a+="4"
 elif S[5]==".##....##":a+="5"
 elif S[5]=="...##....":a+="7"
 else:
  if S[2]==".......##":a+="3"
  elif S[2]=="##.......":a+="6"
  else:
   if S[4]==".......##":a+="9"
   else:a+="8"
print(a)