'''
역방향 그래프를 사용하여 이미 방문한 곳이라면 함수 종료
    - 리스트가 10000개의 주소를 사용해야 하는데 가능할까 .?
    - "일단해봐"

'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, su1, su2, n):
    visited = [0] * n
    queue = deque()
    queue.append(su1)
    queue.append(su2)
    visited[su1] = 1
    visited[su2] = 1

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if visited[v]:
                return v + 1
            visited[v] = 1
            queue.append(v)

    return -1


T = int(input())

def main():
    for _ in range(T):
        n = int(input())
        graph = [[] * n for _ in range(n)]
        for _ in range(n - 1):
            a, b = map(int, input().split())
            graph[b - 1].append(a - 1)
        su1, su2 = map(int, input().split())
        su1 -= 1
        su2 -= 1

        print(bfs(graph, su1, su2, n))

main()