'''
이중 우선순위 큐 :
- 연산 명령에 따라 우선순위가 가장 높은 데이터 or 낮은 데이터 중 하나 삭제
1. 데이터 삽입
2. 데이터 삭제
    2-1. 우선순위가 가장 높은 것 삭제
    2-2. 우선순위기 가장 낮은 것 삭제

Q에 저장된 각 정수의 값 자체를 우선순위로 간주

풀이:
O(k) 안에 풀어야 한다.
I n : 정수 n을 삽입
D 1 : 최댓값 삭제
D -1 : 최솟값 삭제
만약 Q가 비어있는데 적용할 연산이 D라면 연산 무시 가능
'''

import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    visited = [0] * k       # 최대힙, 최소힙 상태를 공유하기 위한 visited
    max_pq, min_pq = [], [] # max, min을 각각 구분
    for i in range(k):
        order, val = input().split()
        if order == 'I':
            heapq.heappush(max_pq, (-int(val), i))
            heapq.heappush(min_pq, (int(val), i))
            visited[i] = 1
        else:
            if val == '1':
                # min_pq에서 처리됬다면 pop
                while max_pq and not visited[max_pq[0][1]]:
                    heapq.heappop(max_pq)
                if max_pq:
                    visited[max_pq[0][1]] = 0
                    heapq.heappop(max_pq)
            else:
                # max_pq에서 처리됬다면 pop
                while min_pq and not visited[min_pq[0][1]]:
                    heapq.heappop(min_pq)
                if min_pq:
                    visited[min_pq[0][1]] = 0
                    heapq.heappop(min_pq)

    while min_pq and not visited[min_pq[0][1]]:
        heapq.heappop(min_pq)
    while max_pq and not visited[max_pq[0][1]]:
        heapq.heappop(max_pq)

    if max_pq and min_pq:
        print(f'{-max_pq[0][0]} {min_pq[0][0]}')
    else:
        print("EMPTY")