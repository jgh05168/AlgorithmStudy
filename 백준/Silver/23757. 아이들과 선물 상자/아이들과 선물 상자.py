'''
N개의 선물상자, 선물상자에는 현재 담겨있는 선물의 개수가 적혀있음
M명의 선물 받을 아이들

상자에 자신이 원하는 것보다 적은 개수의 선물이 들어있다면 실망한다.

한명이라도 실망하지 않고 모두가 선물을 가져갈 수 있는지 궁금하다!


풀이 :
- 선물상자는 우선순위큐에 저장
- 선물이 가장 많은 상자에서 현재 아이가 선물을 가져갈 수 있다면 선물상자의 선물에서 뺀 뒤 다시 힙큐에 저장
- 아닌 경우 반복문 종료
'''

import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
present_boxes = list(map(int, input().split()))
children = list(map(int, input().split()))

pq = []
# heapq를 위해 재정렬
for pr_cnt in present_boxes:
    heapq.heappush(pq, -pr_cnt)

for need_pr_cnt in children:
    max_pr = -heapq.heappop(pq)     # 음수로 max를 저장했으므로 -를 붙여 원래 개수로 돌려놔야 한다.
    if need_pr_cnt > max_pr:
        print(0)
        break
    else:
        heapq.heappush(pq, -(max_pr - need_pr_cnt))
else:
    print(1)