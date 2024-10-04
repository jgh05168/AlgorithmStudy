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

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(idx, core_cnt, lines):
    global ans, max_core, line_set
    # 가지치기
    if core_cnt + (cores - idx) < max_core:
        return
    # 모든 경우가 가능하다면
    if idx == cores:
        if max_core < core_cnt:
            max_core = core_cnt
            ans = lines
        else:
            ans = min(ans, lines)
        return
    r, c = core_list[idx]
    for d in range(len(dr)):
        tmp = set()
        nr, nc = r + dr[d], c + dc[d]
        flag = 0
        while 0 <= nr < n and 0 <= nc < n:
            if (nr, nc) in line_set:
                flag = 1
                break
            else:
                tmp.add((nr, nc))
                nr, nc = nr + dr[d], nc + dc[d]
        # 만약 무리없이 다 이어졌다면,
        if not flag:
            line_set.update(tmp)
            dfs(idx + 1, core_cnt + 1, lines + len(tmp))
            line_set = line_set.difference(tmp)
        # 이어지지 않았다면, 이어서 진행
    dfs(idx + 1, core_cnt, lines)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 0. 코어 위치 찾기
    core_list = []
    line_set = set()
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                core_list.append((i, j))
                line_set.add((i, j))
    cores = len(core_list)

    ans, max_core = n * n, 0
    # 1. 코어 재귀들어가기
    dfs(0, 0, 0)     # idx, core, lines

    print(f'#{tc} {ans}')