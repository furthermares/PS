import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())

max_ans, min_ans = -sys.maxsize, sys.maxsize

def dfs(turn, ans_cur):
    global add, sub, mul, div, max_ans, min_ans
    if turn == N-1:
        max_ans = max(max_ans, ans_cur)
        min_ans = min(min_ans, ans_cur)
    else:
        if add:
            add-=1
            dfs(turn+1, ans_cur + A[turn+1])
            add+=1
        if sub:
            sub-=1
            dfs(turn+1, ans_cur - A[turn+1])
            sub+=1
        if mul:
            mul-=1
            dfs(turn+1, ans_cur * A[turn+1])
            mul+=1
        if div:
            div-=1
            dfs(turn+1, int(ans_cur / A[turn+1]))
            div+=1

dfs(0, A[0])
print(max_ans)
print(min_ans)