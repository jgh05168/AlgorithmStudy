'''
그 지역의 아이템들을 이용해 서바이벌

양방향 그래프, 수색 범위 m 이내의 모든 지역의 아이템 습득이 가능할 때, 아이템의 최대 개수

100 * 100 * 100
완탐 + bfs 로 충분히 가능할듯 함

--------틀림-------
최대로 큰 부분부터 방문해야 하므로 heapq 사용하여 탐색 -> 다익스트라

'''

import sys, heapq
input = sys.stdin.readline


def bfs(su):
    global max_ans
    pq = []
    visited[su] = 0
    heapq.heappush(pq, (0, su))
    tmp_cnt = locations[su]

    while pq:
        w, u = heapq.heappop(pq)
        for v, nw in graph[u]:
            new_w = w + nw
            # 만약 수색 범위보다 크면 continue
            if new_w > m:
                continue
            # 만약 다음 방문하는 곳이 이전에 방문한 곳의 weight보다 작다면 continue
            if new_w >= visited[v]:    # 이미 방문한 곳임
                continue
            # 첫방문이라면, 보급상자 총합 업데이트 해주기
            if visited[v] == int(1e9):
                tmp_cnt += locations[v]

            visited[v] = new_w
            heapq.heappush(pq, (new_w, v))

    max_ans = max(max_ans, tmp_cnt)


n, m, r = map(int, input().split())
locations = list(map(int, input().split()))
graph = [[] * n for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))

max_ans = 0
# 한 곳씩 방문해가면서 탐색
for start in range(n):
    visited = [int(1e9)] * n
    bfs(start)

    # tmp_ans = 0
    # # 갈 수 있는 모든 거리의 아이템 가치를 모두 더해준다.
    # # 다익스트라와 같이 쓰이지는 않는다. (따로 쓰임)
    # for i in range(n):
    #     if visited[i] <= m:
    #         tmp_ans += locations[i]

    # max_ans = max(max_ans, tmp_ans)

print(max_ans)