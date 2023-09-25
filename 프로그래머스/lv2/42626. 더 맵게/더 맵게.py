import heapq

def solution(scoville, K):
    try:
        heapq.heapify(scoville)
        cnt = 0
        while scoville[0] < K:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
    
            heapq.heappush(scoville, a + b * 2)
            cnt += 1
    
        return cnt
    except:
        return -1

print(solution([1, 2, 3, 9, 10, 12], 7))