#    우  하  상  좌
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# bfs
def bfs(srow, scol):
    queue = []          # bfs 전용 큐
    queue.append((srow, scol))  # 초기 입력(행 열) 큐에 저장
    country_loc = []    # 방문했던 위치들을 저장하기 위한 배열(추후 인구수 통합에 사용)
    country_loc.append((srow, scol))    # 초기 입력 저장
    visited[srow][scol] = True      # 방문했음 처리
    population = 0      # 초기 인구수 변수 초기화
    check = False       # 인구수 이동이 있었는지 없었는지 확인

    while queue:
        row, col = queue.pop(0)
        population += countries[row][col]       # 인구 이동이 일어난 total 인구수 구하기
        for d in range(len(dr)):                # 4방향 조사
            nrow = row + dr[d]
            ncol = col + dc[d]
            # 만약 방향벡터가 행렬 범위 내 존재하고, 두 나라 인구의 차가 L이상 R이하이며, 방문하지 않은 나라라면
            if 0 <= nrow < N and 0 <= ncol < N and L <= abs(countries[row][col] - countries[nrow][ncol]) <= R and visited[nrow][ncol] == False:
                check = True                    # 인구이동이 한번이라도 일어났음을 표시
                queue.append((nrow, ncol))      # queue 입력
                country_loc.append((nrow, ncol))    # 나라 좌표도 저장
                visited[nrow][ncol] = True      # 나라에 방문했음을 표시

    if check:       # 인구이동이 일어났다면,
        avg_population = population // len(country_loc)     # 전체 나라들의 평균 인구수를 구해줌
        for row, col in country_loc:        # 국경이 열린 나라들에 대해
            countries[row][col] = avg_population    # 평균 인구수로 맞춰주는 과정
        return 1        # 인구이동이 일어났음을 count하여 return
    else:           # 인구이동이 일어나지 않았다면,
        return 0        # 인구이동이 일어나지 않았기 때문에 0 return


N, L, R = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[False] * N for _ in range(N)]       # 처음부터 다시 check
    vis = False                                     # 인구이동이 일어났는지 확인

    # 이중 for문을 사용한 이유는 만약 bfs 실행 시 길이 없어 막혔다면, 다른 방문하지 않은 노드에 대한 탐색 역시 필요하기 때문
    for row in range(N):
        for col in range(N):
            if visited[row][col] == False:
                # for i in range(N):
                #     print(*countries[i])
                # print(cnt)
                check = bfs(row, col)
                if check == 1:
                    vis = True          # 인구이동이 일어남을 표시

    # 인구이동이 일어났는지 확인
    if vis == True:
        cnt += 1
    else:
        break       # 일어나지 않았다면 무한루프를 빠져나옴

print(cnt)
