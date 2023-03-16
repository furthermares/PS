import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(N, number):
    if N == number:
        return 1
    
    s = [set() for _ in range(8)]
    for i,v in enumerate(s, start=1):
        v.add(int(str(N) * i))
    for i in range(1, len(s)):
        
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2:
                        s[i].add(op1 // op2)
                        
        if number in s[i]:
            answer = i + 1
            break
    else:
        return("NO")
    return answer

K = int(input())
for _ in range(int(input())):
    print(solution(K, int(input())))