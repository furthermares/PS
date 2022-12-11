import sys
def input(): return sys.stdin.readline().rstrip()

W, H = list(map(int,input().split()))
h = list(map(int,input().split()))
h.insert(0,0); h.append(0)

#cnt_black=0
#cnt_white=0
cnt_blue=0
for i in range(H):
    for j in range(1,W+1):
        if j<=h[i+1]:
            #cnt_black+=1
            pass
        elif max(h[:i+1]) >= j and max(h[i+2:]) >=j:
            cnt_blue+=1
        else:
            #cnt_white+=1
            pass

print(cnt_blue)