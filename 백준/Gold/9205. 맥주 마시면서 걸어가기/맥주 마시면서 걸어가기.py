'''
1. 입력들 graph로 연결

2. x + y <= 1000이면 갈 수 있는 거리다

3. abs(현재 x - 도착지 x) + abs(현재 y - 도착지 y) <= 1000이라면 happy

4. 맥주 개수를 굳이 count 해 줄 필요는 없다. - 어차피 편의점 들리면 다시 full로 채워질 것
'''

import sys
input = sys.stdin.readline
T = int(input())

def bfs(sx, sy):
    queue = [(sx, sy)]
    while queue:
        x, y = queue.pop(0)
        # 만약 현재 위치에서 페스티벌까지 갈 수 있다면
        if abs(x - festivalx) + abs(y - festivaly) <= 1000:
            return 'happy'
        else:
            for idx, convenience in enumerate(convenience_stores):
                nx, ny = convenience[0], convenience[1]
                # 만약 편의점이 맥주가 다 떨어지기 전에 존재한다면
                if not visited[idx] and abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append((nx, ny))
                    visited[idx] = 1

    return 'sad'

for _ in range(T):
    # input
    n = int(input())
    convenience_stores = [0] * n
    homex, homey = map(int, input().split())
    for i in range(n):
        storex, storey = map(int, input().split())
        convenience_stores[i] = (storex, storey)
    festivalx, festivaly = map(int, input().split())

    visited = [0] * (n + 1)
    print(bfs(homex, homey))