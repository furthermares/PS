def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) and collected[-1] < num and k:
            collected.pop()
            k -= 1
        if not k:
            collected += list(number[i:])
            break
        collected.append(num)
    
    collected = collected[:-k] if k else collected
    answer = ''.join(collected)
    return answer