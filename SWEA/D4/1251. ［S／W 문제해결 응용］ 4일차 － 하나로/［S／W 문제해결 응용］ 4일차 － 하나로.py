T = int(input())

def per(i, dist, next):
    global turnel
    if i == 2:
        x1, y1= x_list[dist[0]], y_list[dist[0]]
        x2, y2 = x_list[dist[1]], y_list[dist[1]]
        weight = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
        turnel.append((dist[0], dist[1], weight))
        return
    for j in range(next, N):
        if not selected[j]:
            selected[j] = 1
            per(i + 1, dist + [j], j)
            selected[j] = 0


def find_set(x):
    if island[x] != x:
        island[x] = find_set(island[x])
    return island[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        island[y] = x
    else:
        island[x] = y


for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    selected = [0] * N

    turnel = []
    per(0, [], 0)

    turnel.sort(key=lambda x: x[2])

    # kruskal
    island = [i for i in range(N)]

    visited = 0
    min_l = 0
    for u, v, w in turnel:
        if find_set(u) != find_set(v):
            union(u, v)
            min_l += E * (w ** 2)
            visited += 1
            if visited == N - 1:
                break

    print(f'#{tc} {round(min_l)}')