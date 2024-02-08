import sys, heapq
input = sys.stdin.readline


def solution(operations):
    answer = []
    pq = []
    for idx in range(len(operations)):
        tmp = list(operations[idx].split())
        if tmp[0] == 'I':
            heapq.heappush(pq, int(tmp[1]))
        elif pq:
            if tmp[0] == 'D' and tmp[1] == '-1':
                heapq.heappop(pq)
            else:
                pq.pop()
                pq.sort()
    pq.sort()
    if len(pq):
        answer = [pq[-1], pq[0]]
    else:
        answer = [0, 0]

    return answer