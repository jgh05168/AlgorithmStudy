'''
n x n
한개의 cell 에는 1개의 core 혹은 전선이 올 수 있음
- 전선은 직선으로만 설치 가능
- 교차해서는 안된다
- 가장자리에 위치한 코어는 이미 전원이 연결된 것으로 간주한다
- 최대한 많은 코어에 전선을 연결했을 경우, 전선 길이의 합을 구하고자 함

최대 12 x 12
코어 개수 12개 이하
전원이 연결되지 않은 코어 존재 가능

풀이:
이미 지나간 코어를 행 x 열 따로 저장하는 방법은 ?
set.update(), set.remove
1. 프로세스 위치들 저장
2. 뽑아서 사용 - 12! x 5
- 전원이 연결되는 경우가 아니라면 의미없음
- 전원이 연결되는 경우에 대해 가지치기 진행
    - 최대 경우보다 작다면 return
'''

dr = [0, 1, 0, -1]  # 방향: 오른쪽, 아래, 왼쪽, 위쪽
dc = [1, 0, -1, 0]


def dfs(idx, core_cnt, lines):
    global ans, max_core
    # 가지치기: 남은 코어를 모두 연결해도 현재 최대 코어 수에 못 미치면 중단
    if core_cnt + (cores - idx) < max_core:
        return

    # 모든 코어를 처리했으면 결과 갱신
    if idx == cores:
        if max_core < core_cnt:
            max_core = core_cnt
            ans = lines
        elif max_core == core_cnt:
            ans = min(ans, lines)
        return

    # 현재 코어 위치
    r, c = core_list[idx]

    # 4방향으로 전선 설치 시도
    for d in range(4):
        tmp = []
        nr, nc = r + dr[d], c + dc[d]
        flag = False

        # 전선을 놓을 수 있는지 확인
        while 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] != 0:  # 이미 전선 또는 코어가 있는 경우
                flag = True
                break
            tmp.append((nr, nc))  # 전선 설치 가능 위치 저장
            nr, nc = nr + dr[d], nc + dc[d]

        # 전선을 놓을 수 있다면
        if not flag:
            # 전선 설치
            for tr, tc in tmp:
                grid[tr][tc] = 2  # 2는 전선을 의미

            # 다음 코어 탐색
            dfs(idx + 1, core_cnt + 1, lines + len(tmp))

            # 백트래킹: 전선을 다시 없앰
            for tr, tc in tmp:
                grid[tr][tc] = 0

    # 현재 코어를 연결하지 않고 넘어가는 경우
    dfs(idx + 1, core_cnt, lines)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 0. 코어 위치 찾기 (가장자리 코어는 제외)
    core_list = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if grid[i][j] == 1:
                core_list.append((i, j))
    cores = len(core_list)

    # 결과 초기화
    ans, max_core = float('inf'), 0

    # 1. DFS 탐색 시작
    dfs(0, 0, 0)

    print(f'#{tc} {ans}')
