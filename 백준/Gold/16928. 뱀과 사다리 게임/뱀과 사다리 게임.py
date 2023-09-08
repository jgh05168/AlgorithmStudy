
N, M = map(int, input().split())

ladders = [0] * 101
snakes = [0] * 101
visited = [0] * 101
for _ in range(N):
    fro, t = map(int, input().split())
    ladders[fro] = t
for _ in range(M):
    fro, t = map(int, input().split())
    snakes[fro] = t

queue = [(0, 1)]
visited[1] = 1
while queue:
    cnt, start = queue.pop(0)
    if start == 100:
        print(cnt)
        break
    else:
        cnt += 1
        for i in range(1, 7):
            nstart = start + i
            if 0 <= nstart < 101 and not visited[nstart]:
                # 사다리가 있는 경우
                if ladders[nstart]:
                    nstart = ladders[nstart]
                # 뱀이 있는 경우
                elif snakes[nstart]:
                    nstart = snakes[nstart]
                else:
                    nstart = start + i
                visited[nstart] = 1
                queue.append((cnt, nstart))