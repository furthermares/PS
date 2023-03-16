import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif not len(scoville):
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + 2 * min2)
        answer += 1
    return answer