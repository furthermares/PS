import sys
def input(): return sys.stdin.readline().rstrip()

bingo=[[0]*5 for _ in range(5)]
bingo_ans=[[0]*5 for _ in range(5)]
bingo_check=[[False]*5 for _ in range(5)]

for i in range(5):
    bingo[i] = list(map(int,input().split()))
for i in range(5):
    bingo_ans[i] = list(map(int,input().split()))

def func():
    cnt=0
    for a in range(5):
        for b in range(5):
            
            num = bingo_ans[a][b]
            turn = 5*a+b+1
            
            for k in range(5):
                for l in range(5):
                    if bingo[k][l] == num:
                        bingo_check[k][l] = True
    
            cnt=0
            if turn >= 12:
                for i in range(5):
                    if (bingo_check[i][0] and bingo_check[i][1] and bingo_check[i][2] and bingo_check[i][3] and bingo_check[i][4]):
                        cnt += 1
                    if (bingo_check[0][i] and bingo_check[1][i] and bingo_check[2][i] and bingo_check[3][i] and bingo_check[4][i]):
                        cnt += 1
                if (bingo_check[0][0] and bingo_check[1][1] and bingo_check[2][2] and bingo_check[3][3] and bingo_check[4][4]):
                    cnt += 1
                if (bingo_check[0][4] and bingo_check[1][3] and bingo_check[2][2] and bingo_check[3][1] and bingo_check[4][0]):
                    cnt+=1
        
                if cnt >= 3:
                    print(turn)
                    return

func()