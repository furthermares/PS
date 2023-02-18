import sys
def input(): return sys.stdin.readline().rstrip()
    
from itertools import combinations, permutations

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

ans = sys.maxsize

def get_score(team):
    score = 0
    for i,j in permutations(team, 2):
       score += S[i-1][j-1]
    return score

for case in combinations(range(N),N//2):
    teamA, teamB = [], []
    for i in range(N):
        if i in case:
            teamA.append(i)
        else:
            teamB.append(i)

    ans = min(ans, abs(get_score(teamA) - get_score(teamB)))

print(ans)