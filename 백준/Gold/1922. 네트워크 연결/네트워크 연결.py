'''
전형적인 MST

- 크루스칼로 풀어보기
'''

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())

    parent = [i for i in range(1, n + 1)]
    graph = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))
    graph.sort(key=lambda x: x[2])      # weight 낮은 순으로 오름차순


    def find(x):
        if parent[x - 1] != x:
            parent[x - 1] = find(parent[x - 1])
        return parent[x - 1]


    def union(x, y):
        rx, ry = find(x), find(y)

        if rx == ry:
            return
        if rx < ry:
            parent[rx - 1] = ry
        else:
            parent[ry - 1] = rx

    cnt = 0
    total = 0
    for u, v, w in graph:
        # 사이클이 발생하지 않는다면
        if find(u) != find(v):
            cnt += 1
            total += w
            union(u, v)
            # MST가 완성되었다면
            if cnt == m:
                break

    print(total)

main()