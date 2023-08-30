dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol):
    queue = []
    queue.append((srow, scol))

    cnt = 0
    while queue:
        row, col = queue.pop(0)
        cnt += 1
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            # 다음 방과 무조건 1차이가 나는 경우에만 큐에 저장
            if 0 <= nrow < N and 0 <= ncol < N and arr[row][col] + 1 == arr[nrow][ncol]:
                queue.append((nrow, ncol))

    return cnt

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    min_room = 10**6
    for i in range(N):
        for j in range(N):
            # 모든 인덱스에서 출발해야 한다.
            cnt = bfs(i, j)
            # cnt가 클 경우와 같은 경우에 대해서 구분해야된다.
            if max_cnt < cnt:
                max_cnt = cnt
                min_room = arr[i][j]
            # 같은 경우, 방이 작은 것으로 업데이트
            elif max_cnt == cnt and min_room > arr[i][j]:
                min_room = arr[i][j]

    print(f'#{tc} {min_room} {max_cnt}')