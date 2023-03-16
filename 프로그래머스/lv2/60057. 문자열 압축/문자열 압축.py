def solution(s):
    answer = len(s)

    for size in range(1, len(s)//2 + 1):
        cnt = 1
        compress = 0
        
        prev = s[:size]
        for i in range(size, len(s) + size, size):
            curr = s[i:i + size]
            if prev == curr:
                cnt += 1
            else:
                compress += size + len(str(cnt)) if 1 < cnt else len(prev)
                prev = curr
                cnt = 1
        answer = min(answer, compress)

    return answer