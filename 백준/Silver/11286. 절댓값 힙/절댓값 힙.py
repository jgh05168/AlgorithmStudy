import sys, heapq
input = sys.stdin.readline

pq = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(pq, (abs(x), x))
    else:
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)