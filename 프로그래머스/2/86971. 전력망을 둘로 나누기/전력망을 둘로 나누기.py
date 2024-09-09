'''
두 전력망이 갖는 송전탑의 개수를 최대한 비슷하게 하기
- 모든 전력망은 연결되어 있다.

풀이:
1. 조합 짜기 (100C2 = 1350)
2. 이후 각각에 대해 bfs 진행
    -> 하나의 네트워크에 대해서 bfs 진행
    -> 이후 set을 사용해 나머지 네트워크와 개수 비교하기
'''

from collections import deque
import sys

input = sys.stdin.readline


def solution(n, wires):
    answer = n

    def bfs(su, sv):
        queue = deque()
        visited = [0] * (n + 1)
        visited[su] = 1
        queue.append(su)

        while queue:
            u = queue.popleft()
            for v in grid[u]:
                if visited[v] or v == sv:
                    continue
                queue.append(v)
                visited[v] = 1
        one, zero = 0, 0
        for i in range(1, n + 1):
            if visited[i]: one += 1
            else: zero += 1
        return abs(one - zero)

    grid = [[] * (n + 1) for _ in range((n + 1))]

    for si, sj in wires:
        grid[si].append(sj)
        grid[sj].append(si)

    disconnected_set = set()
    for u in range(1, n + 1):
        for v in grid[u]:
            if (u, v) not in disconnected_set:
                disconnected_set.add((u, v))
                disconnected_set.add((v, u))
                answer = min(answer, bfs(u, v))

    return answer