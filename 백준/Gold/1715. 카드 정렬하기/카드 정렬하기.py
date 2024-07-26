'''
1. heapq를 사용하여 모두 넣는다.
2. 작은 수 2개씩 빼가면서 더한 다음 다시 heapq에 삽입한다.
3. 루트 힙만 남는다면 반복문 종료 후 출력
'''

import sys, heapq
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    heapq.heappush(pq, int(input()))

if n == 1:
    print(0)
    exit()

ans = 0
while len(pq) > 1:
    x, y = heapq.heappop(pq), heapq.heappop(pq)
    ans += x + y
    heapq.heappush(pq, x + y)
print(ans)