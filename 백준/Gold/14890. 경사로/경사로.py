'''
각 칸에 높이
길 지나다녀보기 : 2차원 배열 모든 모서리 위치부터 출발해본다.

1. 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 바닥이 모두 닿아야 한다.
2. 낮은 칸과 높은 칸의 차이는 1
경사로를 놓을 낮은 칸의 높이는 모두 같아야하고, L개의 칸이 연속되어야 한다.

풀이 : 2번 for문을 돌며 경사 차이가 생길 때, 경사로를 놓아본다.
놓아본 다음, 양 쪽에서 왔다갔다가 가능해야지 갈 수 있는 길로 인정한다.
가능하다면 한 길에 경사로 여러번 놔도 된다.
각 길은 독립적으로 본다.

- 높이가 똑같은 낮은 칸을 카운트하기
- 칸이 다르다면, 경사로를 놓을 수 있는지 체크하기.
- 칸이 낮아지는 경우에는 반대편에서 올 때 체크하면 되니, 건너뛰고 낮은 칸 값으로 업데이트 해주기
- 놓을 수 없는 경우에는 가차없이 continue
- 이미 경사로가 놓여진 칸에 대해서 체크하는 배열 생성

'''

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

ramp = [[0] * n for _ in range(n)]
# 가로부터 체크
for r in range(n):
    check_left, check_right = True, True
    # 왼 -> 오
    lower_height = grid[r][0]
    start = 0
    for c in range(1, n):
        # 만약 높이 차이가 난다면,
        if grid[r][c] > lower_height:
            # 높이가 1차이고, 경사로를 놓을 수 있다면,
            if grid[r][c] - lower_height == 1 and c - start == l:
                # 경사로 배열 업데이트
                for nc in range(start, c):
                    ramp[r][nc] = 1
                # 올라간 높이로 초기화
                lower_height, start = grid[r][c], c
            # 아닌 경우, break(경사로 놓을 수 없음)
            else:
                check_left = False
                break
        # 높이가 낮아진다면,
        elif grid[r][c] < lower_height:
            if lower_height - grid[r][c] == 1:
                # 내려간 높이를 가장 낮은 높이로 업데이트
                lower_height, start = grid[r][c], c
            else:
                check_left = False
                break
        # 만약 l보다 길어지는 경우, start를 한 칸씩 늘려주기
        elif grid[r][c] == lower_height and c - start + 1 > l:
            start += 1
    # 길을 못 놓는 경우라면 다음 행으로
    if not check_left:
        continue

    # 오 -> 왼 (경사로를 지었는지도 체크해주어야 함)
    lower_height = grid[r][n - 1]
    start = n - 1
    flag = False    # 이미 놓인 경사로가 있는지 판단하는 flag
    for c in range(n - 2, -1, -1):
        # 만약 높이 차이가 난다면,
        if grid[r][c] > lower_height:
            # 높이가 1차이고, 경사로를 놓을 수 있다면,
            if grid[r][c] - lower_height == 1 and start - c == l:
                # 경사로 배열 업데이트
                for nc in range(start, c, -1):
                    # 만약 이미 경사로가 놓인 자리라면,
                    if ramp[r][nc]:
                        flag = True
                        break
                    ramp[r][nc] = 1
                # 만약 이미 경사로가 놓였다면, break
                if flag:
                    check_right = False
                    break
                # 올라간 높이로 초기화
                lower_height, start = grid[r][c], c
            # 아닌 경우, break(경사로 놓을 수 없음)
            else:
                check_right = False
                break
        # 높이가 낮아진다면,
        elif grid[r][c] < lower_height:
            if lower_height - grid[r][c] == 1:
                # 내려간 높이를 가장 낮은 높이로 업데이트
                lower_height, start = grid[r][c], c
            else:
                check_right = False
                break
        # 만약 l보다 길어지는 경우, start를 한 칸씩 늘려주기
        elif grid[r][c] == lower_height and start - c + 1 > l:
            start -= 1
    # 길 이동이 가능하다면, ans += 1
    if check_right and check_left:
        ans += 1


# 세로도 같은 방법으로 체크
ramp = [[0] * n for _ in range(n)]
for c in range(n):
    check_left, check_right = True, True
    # 왼 -> 오
    lower_height = grid[0][c]
    start = 0
    for r in range(1, n):
        # 만약 높이 차이가 난다면,
        if grid[r][c] > lower_height:
            # 높이가 1차이고, 경사로를 놓을 수 있다면,
            if grid[r][c] - lower_height == 1 and r - start == l:
                # 경사로 배열 업데이트
                for nr in range(start, r):
                    ramp[nr][c] = 1
                # 올라간 높이로 초기화
                lower_height, start = grid[r][c], r
            # 아닌 경우, break(경사로 놓을 수 없음)
            else:
                check_left = False
                break
        # 높이가 낮아진다면,
        elif grid[r][c] < lower_height:
            if lower_height - grid[r][c] == 1:
                # 내려간 높이를 가장 낮은 높이로 업데이트
                lower_height, start = grid[r][c], r
            else:
                check_left = False
                break
        # 만약 l보다 길어지는 경우, start를 한 칸씩 늘려주기
        elif grid[r][c] == lower_height and r - start + 1 > l:
            start += 1
    # 길을 못 놓는 경우라면 다음 행으로
    if not check_left:
        continue

    # 오 -> 왼 (경사로를 지었는지도 체크해주어야 함)
    lower_height = grid[n - 1][c]
    start = n - 1
    flag = False    # 이미 놓인 경사로가 있는지 판단하는 flag
    for r in range(n - 2, -1, -1):
        # 만약 높이 차이가 난다면,
        if grid[r][c] > lower_height:
            # 높이가 1차이고, 경사로를 놓을 수 있다면,
            if grid[r][c] - lower_height == 1 and start - r == l:
                # 경사로 배열 업데이트
                for nr in range(start, r, -1):
                    # 만약 이미 경사로가 놓인 자리라면,
                    if ramp[nr][c]:
                        flag = True
                        break
                    ramp[nr][c] = 1
                # 만약 이미 경사로가 놓였다면, break
                if flag:
                    check_right = False
                    break
                # 올라간 높이로 초기화
                lower_height, start = grid[r][c], r
            # 아닌 경우, break(경사로 놓을 수 없음)
            else:
                check_right = False
                break
        # 높이가 낮아진다면,
        elif grid[r][c] < lower_height:
            if lower_height - grid[r][c] == 1:
                # 내려간 높이를 가장 낮은 높이로 업데이트
                lower_height, start = grid[r][c], r
            else:
                check_right = False
                break
        # 만약 l보다 길어지는 경우, start를 한 칸씩 늘려주기
        elif grid[r][c] == lower_height and start - r + 1 > l:
            start -= 1
    # 길 이동이 가능하다면, ans += 1
    if check_right and check_left:
        ans += 1

print(ans)