'''
n x n
1. 두 명의 일꾼이 존재함.
    - 가로로 연속되도록  m개의 벌꿀을 선택하고, 선택한 벌통에서 꿀을 채취할 수 있다.
    - 단, 두 명의 일꾼이 선택한 벌통은 겹치면 안된다.
2. 하나의 벌통에서 채취한 꿀은 하나의 용기에 담아야 한다.
    - 꿀의 최대 양은 c이다.
    - c를 초과한다면 꿀의 양이 최대가 되는 벌꿀을 선택한다.
3. 값 계산은 하나의 벌꿀을 제곱한 것들의 합

최댓값 찾기

풀이:
중복 선택 금지
일단 모두 더해보고 안되면 2번 조건을 위해 c가 안 넘는 선에서 다시 찾아보기

여러 경우가 있을 수 있는데, 만약 10인 경우 벌꿀통이 5 5 9 1 이런 경우, 어떤 벌꿀통을 선택하는지에 따라서도 차이가 있음
-> 벌꿀통 선택에도 순열을 사용해야 함 (어차피 m < 5)
'''


def get_cost(tmp_val, honey_cost, honey_list, selected, idx):
    global tmp
    if honey_cost > c:
        return
    tmp = max(tmp, tmp_val)
    for i in range(idx + 1, m):
        if not selected[i]:
            selected[i] = 1
            get_cost(tmp_val + honey_list[i] ** 2, honey_cost + honey_list[i], honey_list, selected, i)
            selected[i] = 0


def dfs(cnt, sr, sc, val):
    global ans, tmp
    if cnt == 2:
        ans = max(ans, val)
        return
    # 1. 가로로 연속된 벌꿀 선택
    if sr > n - m:
        sc = 0
        sr += 1
    for i in range(sr, n):
        if i > sr:
            sc = 0
        for j in range(sc, n - m + 1):
            tmp_list = grid[i][j:j + m]
            selected = [0] * len(tmp_list)
            tmp = 0
            # 2. 벌꿀통을 선택했다면 값 계산해주기(선택한 벌꿀통 내에서)
            get_cost(0, 0, tmp_list, selected, -1)
            dfs(cnt + 1, i, j + m, val + tmp)


t = int(input())
for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    tmp = 0
    dfs(0, 0, 0, 0)       # cnt, sr, sc, val

    print(f'#{tc} {ans}')