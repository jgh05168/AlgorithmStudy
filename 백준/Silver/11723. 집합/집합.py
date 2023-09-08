import sys
input = sys.stdin.readline

M = int(input())
visited = [0] * 20
S = set()
for _ in range(M):
    orders = list(input().split())
    order = orders[0]
    if len(orders) == 2:
        x = orders[1]

    if order == 'add':
        if not visited[int(x) - 1]:
            S.add(int(x))
            visited[int(x) - 1] = 1
    elif order == 'remove':
        if visited[int(x) - 1]:
            S.remove(int(x))
            visited[int(x) - 1] = 0
    elif order == 'check':
        if visited[int(x) - 1]:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if visited[int(x) - 1]:
            S.remove(int(x))
            visited[int(x) - 1] = 0
        else:
            S.add(int(x))
            visited[int(x) - 1] = 1
    elif order == 'all':
        S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        visited = [1] * 20
    else:
        S.clear()
        visited = [0] * 20



