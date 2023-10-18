'''
현재까지 입력으로 주어진 것들 중 가운데 수를 말해야 한다.
그냥 heapq 쓰면 될듯 ..?
'''

import sys, heapq
input = sys.stdin.readline

N = int(input())
max_pq, min_pq = [], []

for i in range(N):
    x = int(input())
    # 값이 같은 경우 max_pq의 처음에 저장하고, 아니면 min_pq에 저장
    if len(max_pq) == len(min_pq):
        heapq.heappush(max_pq, -x)
    else:
        heapq.heappush(min_pq, x)

    # 만약 min_pq의 최댓값이 max_pq의 최솟값보다 크다면, 두개를 바꿔주기
    if len(max_pq) >= 1 and len(min_pq) >= 1 and max_pq[0] * -1 > min_pq[0]:
        max_value = heapq.heappop(max_pq) * -1
        min_value = heapq.heappop(min_pq)

        heapq.heappush(max_pq, min_value * -1)
        heapq.heappush(min_pq, max_value)

    print(max_pq[0] * -1)       # 음수로 저장했기 때문에 -1 곱해주기